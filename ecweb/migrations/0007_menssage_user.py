# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 22:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecweb', '0006_auto_20171118_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='menssage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
