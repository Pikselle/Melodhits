from datetime import datetime as dt
from datetime import date, timedelta
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
from components.MarkovLyricsGenerator import MarkovLyricsGenerator



# Import des données
df_genres = pd.read_csv('data/PaysComplet.csv', sep=',')
df_artistes = df_genres.copy().sort_values(by=['Artiste'])
df_pays = df_genres.copy().sort_values(by=['Pays'])
df_genres_propre = df_genres.copy().sort_values(by=['Genre'])
df_paroles = pd.read_csv('data/my_data.csv')


######################## Fonctions de mise à jour des Graphs page Année  ########################
def update_genres(annee) :
    df4 = df_genres.loc[df_genres['Annee'] == annee]

    sumNb = df4.count()[0]
    number = df4.groupby(['Genre'])['Genre'].count() / sumNb * 100

    my_data = [go.Bar(x=number, y=number.index, orientation='h')]
    my_layout = ({"title": "Genres du Top 100 Spotify en " + str(annee),
                  "yaxis": {"title": "Genres"},
                  "xaxis": {"title": "Nombres de titres"},
                  "showlegend": False})

    fig = go.Figure(data=my_data, layout=my_layout)
    fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total ascending'})
    return fig

def update_pays(annee) :
    df4 = df_genres.loc[df_genres['Annee'] == annee]

    sumNb = df4.count()[0]
    number = df4.groupby(['Pays'])['Pays'].count() / sumNb * 100

    my_data = [go.Bar(x=number, y=number.index, orientation='h')]
    my_layout = ({"title": "Pays du Top 100 Spotify en " + str(annee),
                  "yaxis": {"title": "Pays"},
                  "xaxis": {"title": "Nombres de titres"},
                  "showlegend": False})

    fig = go.Figure(data=my_data, layout=my_layout)
    fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total ascending'})
    return fig

######################## Fin de mise à jour des Graphs page Année  ########################

######################## Fonctions de mise à jour des Graphs page Artiste  ########################
def update_artiste_top(artiste) :
    df4 = df_genres.loc[df_genres['Artiste'] == artiste]

    number = df4.groupby(['Annee'])['Annee'].count()

    my_data = [go.Bar(x=number.index, y=number, orientation='v')]
    my_layout = ({"title": "Présence dans le top 100 de : " + str(artiste),
                  "yaxis": {"title": "Nombre de titres"},
                  "xaxis": {"title": "Année"},
                  "showlegend": False}
                 )

    fig = go.Figure(data=my_data, layout=my_layout)
    fig.update_layout(barmode='stack', xaxis={'tickformat': ',d', "dtick":1})
    fig.update_layout(yaxis={'tickformat': ',d', "dtick": 1})
    fig.update_layout(uniformtext_minsize=1, uniformtext_mode='hide')
    return fig

def update_artiste_genre(artiste) :
    df4 = df_genres.loc[df_genres['Artiste'] == artiste]

    sumNb = df4.count()[0]
    number = df4.groupby(['Genre'])['Genre'].count() / sumNb * 100

    fig = px.pie(df4, values=number, names=number.index, title="Genres")
    return fig

######################## Fin de mise à jour des Graphs page Artiste  ########################
######################## Fonctions de mise à jour des Graphs page Pays  ########################

def update_pays_top(pays) :
    df4 = df_genres.loc[df_genres['Pays'] == pays]
    number = df4.groupby(['Annee'])['Annee'].count()

    my_data = [go.Bar(x=number.index, y=number, orientation='v')]
    my_layout = ({"title": "Présence dans le top 100 de : " + str(pays),
                  "yaxis": {"title": "Nombre de titres"},
                  "xaxis": {"title": "Année"},
                  "showlegend": False}
                 )

    fig = go.Figure(data=my_data, layout=my_layout)
    fig.update_layout(barmode='stack', xaxis={'tickformat': ',d', "dtick":1})
    fig.update_layout(yaxis={'tickformat': ',d', "dtick": 1})
    fig.update_layout(uniformtext_minsize=1, uniformtext_mode='hide')
    return fig

def update_pays_genre(pays) :
    df4 = df_genres.loc[df_genres['Pays'] == pays]

    sumNb = df4.count()[0]
    number = df4.groupby(['Genre'])['Genre'].count() / sumNb * 100

    fig = px.pie(df4, values=number, names=number.index, title="Genres")
    return fig

def update_liste_artistes(pays) :
    df4 = df_genres.loc[df_genres['Pays'] == pays]
    df4 = df4.Artiste.drop_duplicates()
    return df4

######################## Fin de mise à jour des Graphs page Pays  ########################
######################## Fonctions de mise à jour des Graphs page Genre  ########################
def update_genre_top(genre) :
    df4 = df_genres.loc[df_genres['Genre'] == genre]
    number = df4.groupby(['Annee'])['Annee'].count()

    my_data = [go.Bar(x=number.index, y=number, orientation='v')]
    my_layout = ({"title": "Présence dans le top 100 de : " + str(genre),
                  "yaxis": {"title": "Nombre de titres"},
                  "xaxis": {"title": "Année"},
                  "showlegend": False}
                 )

    fig = go.Figure(data=my_data, layout=my_layout)
    fig.update_layout(barmode='stack', xaxis={'tickformat': ',d', "dtick":1})
    fig.update_layout(yaxis={'tickformat': ',d', "dtick": 1})
    fig.update_layout(uniformtext_minsize=1, uniformtext_mode='hide')
    return fig

def update_genre_pays(genre) :
    df4 = df_genres.loc[df_genres['Genre'] == genre]

    sumNb = df4.count()[0]
    number = df4.groupby(['Pays'])['Pays'].count() / sumNb * 100

    fig = px.pie(df4, values=number, names=number.index, title="Pays")
    return fig

def update_liste_artistesG(genre) :
    df4 = df_genres.loc[df_genres['Genre'] == genre]
    df4 = df4.Artiste.drop_duplicates()
    return df4

######################## Fin de mise à jour des Graphs page Genre  ########################
######################## Fonctions de test Carte  ########################
def update_test():
    fig = go.Figure(data=go.Choropleth(
        locations=df_genres['ISO'],
        z=df_genres['Annee'],
        text=df_genres['Pays'],
        colorscale='Inferno',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Years',
    ))

    fig.update_layout(
        width=1000,
        height=620,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        title={
            'text': '<b>Life expectancy by country</b>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
        },
        title_font_color='#525252',
        title_font_size=26,
        font=dict(
            family='Heebo',
            size=18,
            color='#525252'
        ),
        annotations=[dict(
            x=0.5,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.kaggle.com/daniboy370/world-data-by-country-2020">\
                Kaggle / WORLD DATA by country (2020)</a>',
            showarrow=False
        )]
    )
    return fig

######################## Fin de Fonctions de test  ########################
def update_paroles(theme) :
    # Concaténer toutes les paroles en un seul texte
    corpus_paroles = ' '.join(df_paroles['Paroles'])

    # Création de l'instance de MarkovLyricsGenerator avec le corpus de paroles
    kanyai = MarkovLyricsGenerator(corpus=corpus_paroles, order=2, length=8)

    # Génération d'une chanson avec 10 lignes de longueurs aléatoires entre 5 et 10 mots
    chanson = kanyai.gen_song(lines=10, length_range=[5, 10], startswith=theme)

    # Affichage de la chanson générée
    return chanson

