# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(blank=True, max_length=255, verbose_name='first line of the address')),
                ('line2', models.CharField(blank=True, max_length=255, verbose_name='second line of the address')),
                ('line3', models.CharField(blank=True, max_length=255, verbose_name='third line of the address')),
                ('state', models.CharField(blank=True, max_length=100, verbose_name='state')),
                ('postcode', models.CharField(blank=True, max_length=100, verbose_name='postcode')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=60, verbose_name='Email')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='coordinates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='crm.Coordinates'),
        ),
    ]