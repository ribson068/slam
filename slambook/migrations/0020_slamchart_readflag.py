# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-08-21 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slambook', '0019_auto_20200821_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='slamchart',
            name='readflag',
            field=models.BooleanField(default=False),
        ),
    ]
