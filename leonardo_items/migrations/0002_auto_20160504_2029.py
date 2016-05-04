# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=100, null=True, verbose_name='price', blank=True),
        ),
    ]
