# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 22:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject of the email')),
                ('body', models.CharField(blank=True, max_length=10000, verbose_name='body of the email')),
                ('created', models.DateField(auto_now_add=True, verbose_name='when it was created')),
                ('from_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_whom', to='crm.Email')),
                ('to_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_whom', to='crm.Email')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=18, verbose_name='phone number')),
                ('created', models.DateField(auto_now_add=True, verbose_name='when the user was created')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='last time it was modified')),
                ('home_address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Home_Address', to='crm.Address')),
                ('personal_email', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_email', to='crm.Email')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Person_details', to=settings.AUTH_USER_MODEL)),
                ('work_address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Work_address', to='crm.Address')),
                ('work_email', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_email', to='crm.Email')),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
    ]
