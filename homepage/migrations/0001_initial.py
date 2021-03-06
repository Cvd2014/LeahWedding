# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='WeddingParty')),
            ],
        ),
        migrations.CreateModel(
            name='Groom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='WeddingParty')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='WeddingParty')),
                ('role', models.CharField(max_length=200)),
            ],
        ),
    ]
