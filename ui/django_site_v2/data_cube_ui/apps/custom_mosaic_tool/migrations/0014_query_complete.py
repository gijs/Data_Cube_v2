# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0013_auto_20160705_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='complete',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
