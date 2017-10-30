# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-30 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidencyAddressHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_from', models.DateField()),
                ('contact_person_name', models.CharField(max_length=256)),
                ('contact_person_number', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
                ('residence_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IN', 'Inbound'), ('OUT', 'Outbound')], max_length=4)),
                ('id_number', models.CharField(max_length=8)),
                ('college', models.CharField(choices=[('CCS', 'College of Computer Science'), ('RVRCOB', 'Ramon V del Rosario College of Business'), ('CLA', 'College of Liberal Arts'), ('SOE', 'School of Economics'), ('GCOE', 'Gokongwei College of Engineering'), ('COL', 'College of Law'), ('BAGCED', 'Brother Andrew Gonzales College of Education')], max_length=5)),
                ('family_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('middle_name', models.CharField(max_length=64, null=True)),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('nationality', models.CharField(max_length=64, null=True)),
                ('home_address', models.CharField(max_length=256)),
                ('phone_number', models.CharField(max_length=64)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=2)),
                ('emergency_contact_name', models.CharField(max_length=64)),
                ('emergency_contact_relationship', models.CharField(max_length=32)),
                ('emergency_contact_number', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=256)),
                ('civil_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widowed')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_units_enrolled', models.PositiveIntegerField()),
                ('date_expected_return', models.DateField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Program')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
        migrations.AddField(
            model_name='residencyaddresshistory',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]
