# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='brideside',
            field=models.BooleanField(default=True),
        ),
    ]
