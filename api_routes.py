from flask import Blueprint, request, jsonify, send_from_directory
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
import os
import json
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pytz

#from app import assistant_workflow

# Crie um Blueprint para as rotas da API
api_blueprint = Blueprint('api_blueprint', __name__)

@api_blueprint.route('/receber_json', methods=['POST'])
def receber_json():
    try:
        # Recebe o JSON da requisição
        data = request.get_json()
        # Extrai os valores do JSON
        nome = data.get('nome')
        horarioinput = data.get('horario')
        idusuario = data.get('idusuario')
        idthread = data.get('idthread')
        opcao = data.get('opcao')
        data_servico_input = data.get('data')
        servicoinput = data.get('servico')
        email=data.get('email')


    except Exception as e:
        return jsonify({"retorno": f"Erro: {str(e)}"}), 500

@api_blueprint.route('/json/horariosdesejados.json', methods=['GET'])
def get_json(filename='horariosdesejados.json'):
    current_directory = os.getcwd()  # Diretório atual
    filename = 'horariosdesejados.json'  # Nome do arquivo
    return send_from_directory(directory=current_directory, path='./horariosdesejados.json')
