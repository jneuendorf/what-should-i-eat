# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 20:24
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0008_ingredient_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='color',
            field=colorfield.fields.ColorField(default='#e9c871', max_length=10),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#2f9de3', max_length=10),
        ),
    ]
