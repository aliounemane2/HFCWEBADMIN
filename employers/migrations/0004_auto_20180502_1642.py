# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-02 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0003_auto_20180502_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='photos/'),
        ),
    ]
