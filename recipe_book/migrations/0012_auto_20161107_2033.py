# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0011_auto_20161107_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientamount',
            name='amount',
            field=models.CharField(default='', max_length=50),
        ),
    ]
