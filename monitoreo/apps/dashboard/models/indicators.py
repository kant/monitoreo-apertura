# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from .querysets import IndicatorQuerySet
from .indicator_types import IndicatorType


class AbstractIndicator(models.Model):
    class Meta:
        abstract = True

    fecha = models.DateField(auto_now_add=True)
    jurisdiccion_nombre = models.CharField(max_length=300)
    jurisdiccion_id = models.CharField(max_length=100, null=True)
    indicador_tipo = models.ForeignKey(IndicatorType, models.CASCADE)
    indicador_valor = models.TextField()

    objects = IndicatorQuerySet.as_manager()


class Indicador(AbstractIndicator):
    class Meta:
        # Nombre en plural para el admin panel de Django
        verbose_name_plural = "Tabla de indicadores de nodos"

    def __unicode__(self):
        string = 'Indicador "{0}" de {1}, {2}'
        return string.format(self.indicador_tipo.nombre,
                             self.jurisdiccion_nombre,
                             self.fecha)

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class IndicadorFederador(AbstractIndicator):
    class Meta:
        # Nombre en plural para el admin panel de Django
        verbose_name_plural = "Tabla de indicadores de nodos federadores"

    def __unicode__(self):
        string = 'Indicador "{0}" de {1}, {2}'
        return string.format(self.indicador_tipo.nombre,
                             self.jurisdiccion_nombre,
                             self.fecha)

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class IndicadorRed(models.Model):
    class Meta:
        # Nombre en plural para el admin panel de Django
        verbose_name_plural = "Tabla de indicadores de red"
        get_latest_by = 'fecha'

    fecha = models.DateField(auto_now_add=True)
    indicador_tipo = models.ForeignKey(IndicatorType, models.CASCADE)
    indicador_valor = models.TextField()

    objects = IndicatorQuerySet.as_manager()

    def __unicode__(self):
        string = 'Indicador "{0}" de la Red de Nodos, {1}'
        return string.format(self.indicador_tipo.nombre, self.fecha)

    def __str__(self):
        return self.__unicode__().encode('utf-8')