# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 13:01
from __future__ import unicode_literals

from django.db import migrations

title_to_id_map = {
    "Datos del Sistema Nacional de Información Criminal (SNIC)": "seguridad",
    "Datos abiertos del Ministerio de Desarrollo Social": "desarrollo-social",
    "CKAN": "pami",
    "Datos Económicos Sectoriales y Provinciales": "sspmi",
    "Datos del Instituto Geográfico Nacional": "ign",
    "Datos Programación Macroeconómica": "sspm",
    "Datos Meteorologicos": "smn",
    "Estadisticas Productivas": "siep",
    "Datos Justicia Argentina": "justicia",
    "MSAL": "salud",
    "Ministerio de Energia y Mineria": "energia",
    "Ente Nacional de Comunicaciones (ENACOM)": "enacom",
    "Datos de la Ciencia y la Tecnología Argentina": "mincyt",
    "Autoridad de Cuenca Matanza Riachuelo": "acumar",
    "ARSAT": "arsat",
    "Datos APN": "otros",
    "Datos Modernización": "modernizacion",
    "Datos Agroindustriales": "agroindustria",
    "Datos de la Jefatura de Gabinete de Ministros": "jgm",
    "Portal de Datos Abiertos ANAC": "anac",
    "Datos Abiertos del Ministerio del Interior, Obras Publicas y Vivienda": "interior",
    "Yvera Datos": "turismo",
    "Datos Abiertos del Ministerio de Ambiente y Desarrollo Sustentable": "ambiente",
    "Datos Transporte": "transporte",
}


def fill_indicators_id(apps, schema_editor):
    Indicador = apps.get_model("dashboard", "Indicador")
    for title, identifier in title_to_id_map.items():
        Indicador.objects.filter(jurisdiccion_nombre=title).update(jurisdiccion_id=identifier)
        print u"Migrados los indicadores de {}".format(identifier)


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('dashboard', '0027_indicador_jurisdiccion_id'),
    ]

    operations = [
        migrations.RunPython(fill_indicators_id, migrations.RunPython.noop),
    ]