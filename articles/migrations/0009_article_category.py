# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-23 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20190423_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='articles.Category'),
        ),
    ]