# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-16 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilte', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('nom', models.CharField(max_length=150)),
                ('profession', models.CharField(max_length=150)),
                ('dateNaiss', models.CharField(max_length=35)),
                ('carte_didentite_nationale', models.IntegerField()),
                ('telephone', models.CharField(max_length=50, null=True, unique=True)),
                ('email', models.CharField(blank=True, max_length=125, null=True)),
                ('adresse', models.CharField(blank=True, max_length=125, null=True)),
                ('idcarte', models.IntegerField()),
                ('prenom1', models.CharField(blank=True, max_length=125, null=True)),
                ('nom1', models.CharField(blank=True, max_length=125, null=True)),
                ('telephone1', models.CharField(blank=True, max_length=125, null=True)),
                ('prenom2', models.CharField(blank=True, max_length=125, null=True)),
                ('nom2', models.CharField(blank=True, max_length=125, null=True)),
                ('telephone2', models.CharField(blank=True, max_length=125, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pointage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUser', models.IntegerField()),
                ('date_et_heures', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
