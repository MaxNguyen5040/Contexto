import dash
from dash import dcc, html, Input, Output
from game_logic import game
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Tabs([
        dcc.Tab(label='Dictionary', children=[
            dcc.Input(id='input-word', type='text', placeholder='Enter a word...', className="mb-2"),
            dbc.Button('Get Definition and Synonyms', id='btn-define', color="primary", className="mb-2"),
            html.Div(id='word-data-output')
        ]),
        dcc.Tab(label='Compare Words', children=[
            dcc.Input(id='input-word', type='text', placeholder='Enter a word...', className="mb-2"),
            dcc.Input(id='compare-word', type='text', placeholder='Enter another word...', className="mb-2"),
            dbc.Button('Compare Words', id='btn-compare', color="secondary", className="mb-2"),
            html.Div(id='compare-output')
        ]),
        dcc.Tab(label='Contexto', children=[
            html.H1('Contexto'),
            html.Div(id='contexto-demo', children=[
                html.Div(className='guess', children=[
                    html.Span('Code'),
                    html.Span('Similarity Score: 85')
                ]),
                html.Div(className='guess', children=[
                    html.Span('Keyboard'),
                    html.Span('Similarity Score: 78')
                ]),
                html.Div(className='guess', children=[
                    html.Span('Mouse'),
                    html.Span('Similarity Score: 65')
                ]),
                html.Div(className='guess', children=[
                    html.Span('Python'),
                    html.Span('Similarity Score: 90')
                ]),
            ]),
        ])
    ])
])

@app.callback(
    [Output('output-div', 'children'),
     Output('guess-history', 'children'),
     Output('score-div', 'children')],
    [Input('submit-button', 'n_clicks'),
     Input('reset-button', 'n_clicks')],
    [dash.dependencies.State('word-input', 'value')]
)
def update_output(submit_clicks, reset_clicks, value):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "", "", ""
    if ctx.triggered[0]['prop_id'] == 'reset-button.n_clicks':
        game.reset()
        return "", "", ""
    if not value:
        return "", "", ""
    result = game.check_guess(value)
    history = game.get_guesses()
    history_list = [html.Li(f"{guess} - {fetch_word_definition(guess)}") for guess in history]
    score = f"Score: {game.score}"
    return result, html.Ul(history_list), score

def update_model_result(n_clicks, text1, text2):
    if n_clicks > 0 and text1 and text2:
        comparison_result = compare_texts(text1, text2)
        if comparison_result is not None:
            return html.Div(f"Model comparison result: {comparison_result}")
    return html.Div("")

@app.callback(
    Output('similarity-output', 'children'),
    [Input('word-dropdown', 'value')]
)
def update_similarity_output(selected_word):
    if selected_word:
        similarities = model.calculate_word_similarity(words)
        similar_words = similarities[selected_word]
        sorted_similar_words = sorted(similar_words.items(), key=lambda item: item[1], reverse=True)
        
        return html.Div([
            html.H3(f"Most Similar Words to '{selected_word}':"),
            html.Ul([html.Li(f"{word}: {score}") for word, score in sorted_similar_words])
        ])
    return html.Div("")

@app.callback(
    [dash.dependencies.Output('game-output', 'children'),
     dash.dependencies.Output('score-output', 'children')],
    [dash.dependencies.Input('btn-submit', 'n_clicks')],
    [dash.dependencies.State('input-word', 'value')]
)
def update_game(n_clicks, input_word):
    global user_score
    if n_clicks and input_word:
        similarity_scores = model.calculate_word_similarity([input_word] + words)
        user_score += 10  # Example scoring logic
        return html.Div(f"Similarity scores: {similarity_scores}"), html.Div(f"Score: {user_score}")
    return html.Div(), html.Div()

def analyze_guesses_and_update_state(guesses, target_word, similarity_threshold=0.5):
    from difflib import SequenceMatcher
    import random
    
    updated_guesses = []
    game_over = False
    message = ""
    
    def calculate_similarity(word1, word2):
        return SequenceMatcher(None, word1, word2).ratio()
    
    for guess in guesses:
        similarity_score = calculate_similarity(guess, target_word)
        updated_guesses.append({
            'guess': guess,
            'similarity_score': round(similarity_score * 100)
        })
        
        if similarity_score >= similarity_threshold:
            game_over = True
            message = f"Congratulations! '{guess}' is very close to the target word '{target_word}'!"
            break
    
    if not game_over:
        encouragement_messages = [
            "Keep going! You're doing great!",
            "Don't give up, you're getting closer!",
            "Nice try! Keep guessing!",
            "You're on the right track, keep it up!",
            "Almost there! Keep thinking!"
        ]
        message = random.choice(encouragement_messages)
    
    return updated_guesses, game_over, message

if __name__ == '__main__':
    app.run_server(debug=True)

