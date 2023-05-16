from dash.dependencies import Input, Output
from app import app
from datetime import datetime as dt
from datetime import date, timedelta

from dash import html
from components.functions import update_genres, update_pays, \
    update_artiste_top, update_artiste_genre, update_pays_genre, update_pays_top, update_liste_artistes, \
    update_genre_top, update_genre_pays, update_liste_artistesG, update_test


######################## Callbacks page Evolution ########################

@app.callback(
   Output('genresGraph', 'figure'),
   [Input('dropdown-publishing', 'value')])

def update_graph_genres(value):
    fig = update_genres(value)
    return fig

@app.callback(
   Output('paysGraph', 'figure'),
   [Input('dropdown-publishing', 'value')])

def update_graph_pays(value):
    fig = update_pays(value)
    return fig

######################## Callbacks page Artistes ########################

@app.callback(
   Output('artisteGenreGraph', 'figure'),
   [Input('dropdown-artistes', 'value')])

def update_graph_artiste_genre(value):
    fig = update_artiste_genre(value)
    return fig

@app.callback(
   Output('artisteTopGraph', 'figure'),
   [Input('dropdown-artistes', 'value')])

def update_graph_artiste_top(value):
    fig = update_artiste_top(value)
    return fig

######################## Callbacks page Pays ########################

@app.callback(
   Output('paysGenreGraph', 'figure'),
   [Input('dropdown-pays', 'value')])

def update_graph_pays_genre(value):
    fig = update_pays_genre(value)
    return fig

@app.callback(
   Output('paysTopGraph', 'figure'),
   [Input('dropdown-pays', 'value')])

def update_graph_pays_top(value):
    fig = update_pays_top(value)
    return fig

@app.callback(
    Output(component_id='proprePays', component_property='children'),
    Input(component_id='dropdown-pays', component_property='value')
)
def update_output_div(value):
    liste = update_liste_artistes(value)
    return html.Ul([html.Li(x) for x in liste])

######################## Callbacks page Genres ########################

@app.callback(
   Output('genrePaysGraph', 'figure'),
   [Input('dropdown-genre', 'value')])

def update_graph_genre_pays(value):
    fig = update_genre_pays(value)
    return fig

@app.callback(
   Output('genreTopGraph', 'figure'),
   [Input('dropdown-genre', 'value')])

def update_graph_genre_top(value):
    fig = update_genre_top(value)
    return fig

@app.callback(
    Output(component_id='propreGenre', component_property='children'),
    Input(component_id='dropdown-genre', component_property='value')
)
def update_output_div2(value):
    liste = update_liste_artistesG(value)
    return html.Ul([html.Li(x) for x in liste])

######################## Callbacks page TEST CARTE ########################

@app.callback(
    Output(component_id='graphtest', component_property='children'),
    Input(component_id='dropdown-artistes', component_property='value')
)
def update_output_div2(value):
    graph = update_test()
    return graph