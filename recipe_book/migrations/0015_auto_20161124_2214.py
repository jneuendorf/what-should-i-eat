# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0014_auto_20161110_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
