# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr_app', '0003_auto_20160225_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]