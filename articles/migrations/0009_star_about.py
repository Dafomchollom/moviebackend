# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-03 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20190503_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='about',
            field=models.TextField(blank=True, default='no information'),
        ),
    ]