# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import recipe_book.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0006_auto_20161101_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(blank=True, upload_to=recipe_book.models.ingredient_image_location),
        ),
    ]
