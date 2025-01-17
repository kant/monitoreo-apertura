#! coding: utf-8

import json
import logging
from django_rq import job

from pydatajson.core import DataJson
from pydatajson.federation import harvest_catalog_to_ckan
from django_datajsonar.models import Node, Dataset
from .helpers import generate_task_log
from .models import HarvestingNode, FederationTask
from .strings import UNREACHABLE_CATALOG, TASK_ERROR

LOGGER = logging.getLogger(__name__)


@job('federation')
def federation_run(node=None):
    harvesting_nodes = HarvestingNode.objects.filter(enabled=True)
    for harvester in harvesting_nodes:
        task = FederationTask.objects.create(harvesting_node=harvester, node=node)
        federate_catalogs(task)


@job('federation')
def federate_catalogs(task):
    portal_url = task.harvesting_node.url
    apikey = task.harvesting_node.apikey
    nodes = [task.node] if task.node else Node.objects.filter(indexable=True)
    for harvestable_node in nodes:
        federate_catalog.delay(harvestable_node, portal_url, apikey, task.pk)
    # Necesario para usar el abstractTaskAdmin. Terminar todas las tareas
    task.status = FederationTask.FINISHED
    task.save()


@job('federation', timeout=1800)
def federate_catalog(node, portal_url, apikey, task_id):
    task = FederationTask.objects.get(pk=task_id)
    catalog = get_catalog_from_node(node)
    catalog_id = node.catalog_id
    msg = u"Catálogo: %s\n" % node.catalog_id
    if not catalog:
        msg += UNREACHABLE_CATALOG.format(node.catalog_id)
        FederationTask.info(task, msg)
        LOGGER.warning(msg)
        return msg
    catalog.generate_distribution_ids()
    valid, invalid, missing = sort_datasets_by_condition(node, catalog)

    try:
        harvested_ids, federation_errors = harvest_catalog_to_ckan(catalog, portal_url, apikey, catalog_id, list(valid),
                                                                   origin_tz=node.timezone,
                                                                   dst_tz=task.harvesting_node.timezone)
        msg += generate_task_log(catalog, catalog_id, invalid, missing, harvested_ids, federation_errors)
        FederationTask.info(task, msg)
        LOGGER.warning(msg)
        return msg

    except Exception as e:
        msg += TASK_ERROR.format(catalog_id, list(valid), e)
        FederationTask.info(task, msg)
        LOGGER.warning(msg)
        return msg


def sort_datasets_by_condition(node, catalog):
    catalog_report = catalog.validate_catalog()
    valid_set = {ds['identifier'] for ds in catalog_report['error']['dataset'] if ds['status'] == 'OK'}
    invalid_set = {ds['identifier'] for ds in catalog_report['error']['dataset'] if ds['status'] == 'ERROR'}
    dataset_models = set(Dataset.objects.filter(catalog__identifier=node.catalog_id, indexable=True, present=True,)
                         .values_list("identifier", flat=True))
    valid_datasets = dataset_models.intersection(valid_set)
    invalid_datasets = dataset_models.intersection(invalid_set)
    missing_datasets = dataset_models - (valid_datasets | invalid_datasets)
    return valid_datasets, invalid_datasets, missing_datasets


def get_catalog_from_node(node):
    try:
        catalog = DataJson(node.catalog_url, catalog_format=node.catalog_format)
        return catalog

    except Exception:
        dictionary = json.loads(node.catalog)
        if dictionary:
            catalog = DataJson(dictionary)
            return catalog

        return None
