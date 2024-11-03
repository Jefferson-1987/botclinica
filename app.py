from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
import os.path
import json
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from api_routes import api_blueprint  # Importa o Blueprint do arquivo api_routes.py

# Crie o app Dash com tema externo
app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])
server = app.server  # O server Flask subjacente

# Registra o Blueprint da API no servidor Flask
server.register_blueprint(api_blueprint, url_prefix='/api')

# Escopos para acesso à Google Agenda
app.layout = html.Div([
    html.H1("Formulário de Serviço"),
    
    # Entrada de data
    html.Label("Data do Serviço:"),
    dcc.Input(id='input-data', type='text', placeholder='dd/mm/aaaa'),
    
    # Entrada de serviço
    html.Label("Tipo de Serviço:"),
    dcc.Input(id='input-servico', type='text', placeholder='Nome do serviço'),
    
    # Entrada de hora
    html.Label("Hora do Serviço:"),
    dcc.Input(id='input-hora', type='text', placeholder='hh:mm'),
    
    # Entrada de código (1 a 5)
    html.Label("Código (1-5):"),
    dcc.Slider(
        id='input-codigo',
        min=1,
        max=5,
        step=1,
        marks={i: str(i) for i in range(1, 6)},
        value=1
    ),
    
    # Botão de submissão
    html.Button('Enviar', id='submit-button', n_clicks=0),
    
    # Área para exibir a saída
    html.Div(id='output-div', style={'marginTop': 20})
])
# Callback para atualizar o conteúdo do dashboard após submissão
@app.callback(
    Output('output-div', 'children'),
    Input('submit-button', 'n_clicks'),
    [Input('input-data', 'value'),
     Input('input-servico', 'value'),
     Input('input-hora', 'value'),
     Input('input-codigo', 'value')]
)
def update_output(n_clicks, data, servico, hora, codigo):
    if n_clicks > 0:
        return html.Div([
            html.P(f"Data: {data}"),
            html.P(f"Serviço: {servico}"),
            html.P(f"Hora: {hora}"),
            html.P(f"Código: {codigo}")
        ])
    return "Preencha os campos e clique em 'Enviar'."

# assistant_workflow()
if __name__ == "__main__":
    app.run_server(debug=False, port=8080, host="0.0.0.0")
