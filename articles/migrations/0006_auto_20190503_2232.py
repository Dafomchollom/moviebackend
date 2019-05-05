# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-03 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_advert_advert_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'star',
                'verbose_name_plural': 'stars',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='star',
            field=models.ManyToManyField(default='none', to='articles.Star'),
        ),
    ]
