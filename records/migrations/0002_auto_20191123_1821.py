# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-23 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='check_out',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
