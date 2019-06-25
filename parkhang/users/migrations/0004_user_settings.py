# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-14 11:22
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180926_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='settings',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
