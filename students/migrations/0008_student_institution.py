# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-05 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0013_auto_20171105_0613'),
        ('students', '0007_auto_20171104_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='institution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='institutions.Institution'),
            preserve_default=False,
        ),
    ]
