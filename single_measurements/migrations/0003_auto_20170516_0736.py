# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_measurements', '0002_auto_20170516_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlemeasurements',
            name='formtype',
            field=models.CharField(choices=[('ltr', 'Liter'), ('kg', 'Kilogram'), ('pcs', 'Pieces')], max_length=10, verbose_name='Units'),
        ),
    ]
