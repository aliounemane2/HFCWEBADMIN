# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-04 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statisque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField(auto_now_add=True)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.utilisateur2')),
            ],
        ),
    ]
