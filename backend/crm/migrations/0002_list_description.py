# Generated by Django 2.0 on 2018-02-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Purpose of the list'),
        ),
    ]
