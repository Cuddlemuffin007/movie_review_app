# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr_app', '0005_auto_20160226_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='avg_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
