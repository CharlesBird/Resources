# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-31 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=32, verbose_name='\u72b6\u6001'),
            preserve_default=False,
        ),
    ]
