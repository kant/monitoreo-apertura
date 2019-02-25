# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-18 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0041_centralnode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centralnode',
            options={'verbose_name': 'Nodo central'},
        ),
        migrations.AlterModelOptions(
            name='federationtask',
            options={'verbose_name_plural': 'Corridas de federaci\xf3n'},
        ),
        migrations.AlterModelOptions(
            name='indicador',
            options={'verbose_name_plural': 'Tabla de indicadores de nodos'},
        ),
        migrations.AlterModelOptions(
            name='indicadorfederador',
            options={'verbose_name_plural': 'Tabla de indicadores de nodos federadores'},
        ),
        migrations.AlterModelOptions(
            name='indicadorred',
            options={'get_latest_by': 'fecha', 'verbose_name_plural': 'Tabla de indicadores de red'},
        ),
        migrations.AlterModelOptions(
            name='indicatorsgenerationtask',
            options={'verbose_name_plural': 'Corridas de indicadores'},
        ),
        migrations.AlterModelOptions(
            name='reportgenerationtask',
            options={'verbose_name_plural': 'Reportes de indicadores'},
        ),
    ]