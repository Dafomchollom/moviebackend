# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-16 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190316_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='postdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
