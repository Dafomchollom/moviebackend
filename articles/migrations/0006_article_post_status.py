# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-23 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20190316_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Post_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
