# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20171104_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(choices=[('IN', 'Inbound'), ('OUT', 'Outbound')], max_length=3),
        ),
    ]