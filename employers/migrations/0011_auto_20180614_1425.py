# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-14 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0010_auto_20180604_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='carte_didentite_nationale',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employers',
            name='email',
            field=models.CharField(max_length=125, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employers',
            name='telephone',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
