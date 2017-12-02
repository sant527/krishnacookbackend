# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 18:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_auto_20170516_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='density_kg_per_lt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Density (kg/lt)'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='density_pcs_per_kg',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Density (pcs/kg)'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='density_pcs_per_lt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Density (pcs/lt)'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
