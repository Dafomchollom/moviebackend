# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-03 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_star_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='postdate',
            field=models.DateTimeField(),
        ),
    ]