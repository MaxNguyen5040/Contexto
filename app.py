import dash
from dash import dash_core_components as dcc
from dash import dash_html_components as html
from dash import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Contexto Game"), className="text-center")
    ]),
    dbc.Row([
        dbc.Col(dcc.Input(id="word-input", type="text", placeholder="Enter your guess"), width=8),
        dbc.Col(dbc.Button("Submit", id="submit-button", color="primary"), width=4)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id="output-div"), width=12)
    ])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)