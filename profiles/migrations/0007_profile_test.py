# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-23 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20161117_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='test',
            field=models.TextField(default='description'),
        ),
    ]