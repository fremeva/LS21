# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 09:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RobotMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('search_key', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('ON_GOING', 'On Going'), ('ERROR', 'Error'), ('STOPPED', 'Stopped'), ('FINISHED', 'Finished')], default='CREATED', max_length=15)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TasksRobot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_celey_id', models.CharField(max_length=255)),
                ('task_label', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('STARTED', 'Started'), ('FAILURE', 'Failure'), ('REVOKED', 'Revoked'), ('SUCCESS', 'Success')], default='PENDING', max_length=20)),
                ('robot_monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='apiscrap.RobotMonitor')),
            ],
        ),
    ]
