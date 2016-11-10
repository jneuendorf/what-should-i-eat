# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 18:28
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0010_auto_20161104_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#e9c871', max_length=10),
        ),
        migrations.AlterField(
            model_name='ingredientamount',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipe_book.Recipe'),
        ),
    ]