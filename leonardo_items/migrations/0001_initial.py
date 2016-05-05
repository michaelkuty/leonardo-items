# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('type', models.CharField(max_length=20, verbose_name='type', choices=[(b'text', 'text'), (b'email', 'e-mail address'), (b'integer', 'integer'), (b'boolan', 'boolan True / False'), (b'float', 'float'), (b'date', 'Date'), (b'longtext', 'long text'), (b'checkbox', 'checkbox'), (b'select', 'select'), (b'radio', 'radio'), (b'multiple-select', 'multiple select'), (b'hidden', 'hidden'), (b'file', 'File'), (b'image', 'Image')])),
                ('choices', models.CharField(help_text='Comma-separated', max_length=1024, verbose_name='choices', blank=True)),
                ('help_text', models.CharField(help_text='Optional extra explanatory text beside the field', max_length=1024, verbose_name='help text', blank=True)),
                ('default_value', models.CharField(help_text='Optional default value of the field', max_length=255, verbose_name='default value', blank=True)),
            ],
            options={
                'ordering': ['ordering', 'id'],
                'verbose_name': 'item attribute',
                'verbose_name_plural': 'item attributes',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(help_text='value of the field', max_length=255, verbose_name='value', blank=True)),
                ('attribute', models.ForeignKey(related_name='values', verbose_name='item', to='leonardo_items.Attribute')),
            ],
            options={
                'verbose_name': 'attribute value',
                'verbose_name_plural': 'attribute value',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('short_description', models.TextField(null=True, verbose_name='short description', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('price', models.IntegerField(null=True, verbose_name='price', blank=True)),
                ('sold', models.BooleanField(default=False, verbose_name='sold')),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('image', models.ForeignKey(blank=True, to='media.Image', null=True)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='item',
            field=models.ForeignKey(related_name='attributes', verbose_name='item', to='leonardo_items.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='attributevalue',
            unique_together=set([('item', 'attribute')]),
        ),
    ]
