# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-05 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20190505_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='movie_name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
