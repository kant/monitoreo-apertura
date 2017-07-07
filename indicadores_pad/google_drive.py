#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Se conecta a una spreadsheet de Google Drive para traer todas las filas

Hay que crear credenciales propias para el proyecto siguiendo el tutorial en
https://developers.google.com/sheets/api/quickstart/python para generar un
client_secret.json con las credenciales necesarias para conectarse al Drive.

Hay que correr el script desde la línea de comandos para configurar por primera
vez las credenciales que van a ~/.credentials/ . La mejor manera de hacerlo es
agregar un ejemplo sencillo de uso de la nueva API en el main() y correrlo de
la línea de comandos.
"""
from __future__ import print_function

import httplib2
import environ
env = environ.Env()
GOOGLE_DRIVE_PROJECT_CREDENTIALS = env('GOOGLE_DRIVE_PROJECT_CREDENTIALS',
                                       default="")
GOOGLE_DRIVE_USER_CREDENTIALS = env('GOOGLE_DRIVE_USER_CREDENTIALS',
                                    default='user_credentials.json')
from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


# If modifying these scopes, delete your previously saved credentials
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
APPLICATION_NAME = 'Monitoreo PAD'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_path = GOOGLE_DRIVE_USER_CREDENTIALS

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(GOOGLE_DRIVE_PROJECT_CREDENTIALS,
                                              SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Generando nuevas credenciales en ' + credential_path)
    return credentials


def get_sheets_service():
    """Usa las credenciales para crear un servicio a google sheets."""
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discovery_url,
                              cache_discovery=False)
    return service


def get_sheet(spreadsheet_id, range_name):
    """Devuelve el rango de una spreadsheet como lista de listas.
    Args:
        spreadsheet_id (str): Id de la google spreadsheet
          Ej.: '1Vx0SjxnX7X-ASBJkXGWarrrnLItFTAs_TlQvxulLEak'
        range_name (str): Rango target. Ej.: 'Tiempo Real!A1:K'

    Returns:
        list: Filas de la planilla.
    """

    service = get_sheets_service()
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    return values


def main():
    """Genera las credenciales necesarias para poder leer Google Spreadsheets.
    Las credenciales serán escritas en el archivo que apunte las variables de 
    entorno GOOGLE_DRIVE_CREDENTIALS y GOOGLE_DRIVE_USER_CREDENTIALS.
    Este proceso es automáticamente ejecutado si se intenta abrir un
    documento sin tener credenciales guardadas en el sistema.
    """
    get_credentials()

if __name__ == '__main__':
    main()