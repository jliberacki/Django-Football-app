# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0002_auto_20180613_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=2)),
            ],
        ),
    ]
