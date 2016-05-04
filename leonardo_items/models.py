try:
    from collections import OrderedDict
except ImportError:
    from django.utils.datastructures import SortedDict as OrderedDict

from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _
from . import settings, utils

try:
    from django.utils.text import slugify
except ImportError:  # pragma: no cover, Django 1.4
    from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class Item(models.Model):

    title = models.CharField(_('title'), max_length=100)
    short_description = models.TextField(
        _('short description'), blank=True, null=True)
    image = models.ForeignKey('media.Image', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    price = models.CharField(_('price'), blank=True, null=True, max_length=100)
    sold = models.BooleanField(_('sold'), default=False)
    featured = models.BooleanField(_('featured'), default=False)

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')

    def __str__(self):
        return self.title

FIELD_TYPES = utils.get_object(settings.LEONARDO_ITEMS_FIELD_TYPES)


def get_type_choices():
    return [r[:2] for r in
            utils.get_object(settings.LEONARDO_ITEMS_FIELD_TYPES)]


@python_2_unicode_compatible
class Attribute(models.Model):

    ordering = models.IntegerField(_('ordering'), default=0)
    title = models.CharField(_('title'), max_length=100)
    name = models.CharField(_('name'), max_length=100)
    type = models.CharField(
        _('type'), max_length=20, choices=lazy(get_type_choices, list)())
    choices = models.CharField(
        _('choices'), max_length=1024, blank=True,
        help_text=_('Comma-separated'))
    help_text = models.CharField(
        _('help text'), max_length=1024, blank=True,
        help_text=_('Optional extra explanatory text beside the field'))
    default_value = models.CharField(
        _('default value'), max_length=255, blank=True,
        help_text=_('Optional default value of the field'))

    class Meta:
        ordering = ['ordering', 'id']
        verbose_name = _('item attribute')
        verbose_name_plural = _('item attributes')

    def __str__(self):
        return self.title

    def get_choices(self):
        get_tuple = lambda value: (slugify(value.strip()), value.strip())
        choices = [get_tuple(value) for value in self.choices.split(',')]
        if not self.is_required and self.type == 'select':
            choices = BLANK_CHOICE_DASH + choices
        return tuple(choices)

    def get_type(self, **kwargs):
        types = dict((r[0], r[2]) for r in FIELD_TYPES)
        return types[self.type](**kwargs)

    def add_formfield(self, fields, form):
        fields[slugify(self.name)] = self.formfield()

    def formfield(self):
        kwargs = dict(
            label=self.title,
            required=self.is_required,
            initial=self.default_value,
        )
        if self.choices:
            kwargs['choices'] = self.get_choices()
        if self.help_text:
            kwargs['help_text'] = self.help_text
        return self.get_type(**kwargs)


@python_2_unicode_compatible
class AttributeValue(models.Model):
    item = models.ForeignKey(
        Item, related_name='attributes', verbose_name=_('item'))
    attribute = models.ForeignKey(
        Attribute, related_name='values', verbose_name=_('item'))
    value = models.CharField(
        _('value'), max_length=255, blank=True,
        help_text=_('value of the field'))

    def __str__(self):
        return '%s - %s - %s ' % (self.item, self.attribute, self.value)

    class Meta:
        unique_together = (('item', 'attribute'),)
        verbose_name = _('attribute value')
        verbose_name_plural = _('attribute value')
