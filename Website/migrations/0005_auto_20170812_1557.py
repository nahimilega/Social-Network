# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_profile_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fullname',
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
    ]