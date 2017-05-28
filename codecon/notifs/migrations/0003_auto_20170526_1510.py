# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifs', '0002_auto_20170526_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifs', to=settings.AUTH_USER_MODEL),
        ),
    ]
