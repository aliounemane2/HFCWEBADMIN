# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-14 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_parrainage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parrainage',
            name='date_heure_parrainage',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statisque',
            name='date_heure',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
