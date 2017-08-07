# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_point_count_bigint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population', models.CharField(default='', max_length=255)),
                ('subgroup', models.CharField(default='', max_length=255)),
                ('key', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DataSet')),
                ('metric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Metric')),
            ],
        ),
    ]