# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_populate_ids_faltantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportGenerationTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RUNNING', 'Procesando cat\xe1logos'), ('FINISHED', 'Finalizada')], max_length=20)),
                ('created', models.DateTimeField()),
                ('finished', models.DateTimeField(null=True)),
                ('logs', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Env\xedo de reportes',
            },
        ),
    ]