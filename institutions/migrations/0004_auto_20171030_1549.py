# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-30 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0003_institution_memorandum'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='contact_person_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='contact_person_number',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='email',
            field=models.EmailField(max_length=256, null=True),
        ),
    ]
