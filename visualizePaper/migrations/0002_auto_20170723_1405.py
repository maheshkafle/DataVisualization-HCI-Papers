# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 08:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualizePaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]