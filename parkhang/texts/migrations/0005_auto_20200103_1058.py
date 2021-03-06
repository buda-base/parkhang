# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-03 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0004_witness_properties'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4000)),
            ],
        ),
        migrations.AddField(
            model_name='text',
            name='code',
            field=models.CharField(default=0, max_length=4000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='annotation',
            name='type',
            field=models.CharField(choices=[('V', 'Variant'), ('N', 'Note'), ('P', 'Page Break'), ('L', 'Line Break')], default='V', max_length=1),
        ),
    ]
