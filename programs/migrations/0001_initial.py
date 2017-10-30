# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-30 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0004_auto_20171030_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('linkage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('mobility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Mobility')),
            ],
        ),
    ]
