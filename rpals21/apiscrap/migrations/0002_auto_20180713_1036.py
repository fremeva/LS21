# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiscrap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksrobot',
            name='exception',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasksrobot',
            name='meta',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasksrobot',
            name='result',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='robotmonitor',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Created'), ('ON_GOING', 'On Going'), ('STOPPED', 'Stopped'), ('FINISHED', 'Finished')], default='CREATED', max_length=15),
        ),
    ]