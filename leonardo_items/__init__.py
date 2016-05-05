
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


default_app_config = 'leonardo_items.ItemsConfig'


class Default(object):

    optgroup = 'Items Invertory'

    @property
    def apps(self):
        return [
            'leonardo_items'
        ]

    ordering = 1

    @property
    def widgets(self):
        return [
            'leonardo_items.widget.itemlist.models.ItemListWidget'
        ]


class ItemsConfig(AppConfig):
    name = 'leonardo_items'
    verbose_name = _("Item Inventory")

    conf = Default()

default = Default()
