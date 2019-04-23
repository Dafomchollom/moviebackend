# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-23 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190423_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]