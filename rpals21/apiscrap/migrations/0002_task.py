# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiscrap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=200)),
                ('retval', models.TextField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
