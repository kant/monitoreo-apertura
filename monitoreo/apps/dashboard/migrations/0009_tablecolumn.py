# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20170609_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('full_name', models.CharField(max_length=100)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.IndicatorType')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name_plural': 'Columnas de la tabla de indicadores de red',
            },
        ),
    ]