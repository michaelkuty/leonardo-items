
from django.apps import AppConfig


default_app_config = 'leonardo_items.ItemsConfig'


class Default(object):

    optgroup = 'Items Invertory'

    @property
    def apps(self):
        return [
            'leonardo_items'
        ]

    @property
    def widgets(self):
        return [
            'leonardo_items.widget.itemlist.models.ItemListWidget'
        ]


class ItemsConfig(AppConfig):
    name = 'leonardo_items'
    verbose_name = "Item Invertory"

    conf = Default()

default = Default()
