
from django.contrib import admin

from . import models


class AttributeValueAdmin(admin.TabularInline):
    extra = 0
    model = models.AttributeValue


class ItemAttributeAdmin(admin.ModelAdmin):
    extra = 0
    model = models.Attribute
    prepopulated_fields = {'name': ('title',)}


class ItemAdmin(admin.ModelAdmin):
    inlines = [AttributeValueAdmin]
    list_display = ('title',)

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Attribute, ItemAttributeAdmin)
