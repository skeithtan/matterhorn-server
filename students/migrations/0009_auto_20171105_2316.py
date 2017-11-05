# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_student_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.Institution'),
        ),
    ]
