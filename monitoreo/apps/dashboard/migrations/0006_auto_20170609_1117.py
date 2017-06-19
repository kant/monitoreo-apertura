# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-09 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_indicadorred'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='indicador',
            name='indicador_nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.IndicatorType'),
        ),
    ]