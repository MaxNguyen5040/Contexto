import dash
from dash import dash_core_components as dcc
from dash import dash_html_components as html
from dash import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

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
    ]),
    dbc.Row([
        dbc.Col(html.H3("Guess History"), className="text-center"),
        dbc.Col(html.Div(id="guess-history"), width=12)
    ])
], fluid=True)

@app.callback(
    Output('output-div', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('word-input', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks is None:
        return ""
    return f"You guessed: {value}"

@app.callback(
    [Output('output-div', 'children'),
     Output('guess-history', 'children')],
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('word-input', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks is None or not value:
        return "", ""
    result = game.check_guess(value)
    history = game.get_guesses()
    return result, html.Ul([html.Li(guess) for guess in history])

if __name__ == '__main__':
    app.run_server(debug=True)

