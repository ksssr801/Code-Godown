# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-06 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]