# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 20:23
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0007_auto_20161101_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='color',
            field=colorfield.fields.ColorField(default='e9c871', max_length=10),
        ),
    ]
