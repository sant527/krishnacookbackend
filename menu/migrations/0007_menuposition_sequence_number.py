# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20170518_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuposition',
            name='sequence_number',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
