# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import ListWidget

from leonardo_items.models import Item


class ItemListWidget(ListWidget):

    sold = models.NullBooleanField(_('sold'))
    featured = models.NullBooleanField(_('featured'))

    class Meta:
        abstract = True
        verbose_name = _('item list')
        verbose_name_plural = _('list of items')

    def get_items(self, **kwargs):

        if not self.sold and not self.featured:
            return Item.objects.all()

        if self.sold:
            items = Item.objects.filter(**{
                'sold': self.sold,
            })
        else:
            items = Item.objects.filter(**{
                'sold': False,
            })

        if self.featured:
            items = items.filter(featured=self.featured)

        return items
