from dash import dcc
from dash import html
from dash import dash_table
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import time
from components.functions import df_genres, df_genres_propre
import dash
import dash_bootstrap_components as dbc


######################## Fonctions de créations des KPI  ########################

# Couleurs des KPI
color_l=['info',"secondary",'info',"secondary","success","warning","danger"]

def create_card(title, content,color):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="card-title"),
                html.Br(),
                html.H2(content, className="card-subtitle"),
                html.Br(),

                ]
        ),
        color=color, inverse=True
    )
    return(card)

acces_number = df_genres.sum(axis=0)
acces_number[0]= df_genres.Genre.unique().size
acces_number[1] = df_genres['Genre'].value_counts().idxmax()
acces_number[2]=df_genres.Pays.unique().size
acces_number[3] = df_genres['Pays'].value_counts().idxmax()

card1 = create_card("Nombre de genres différents", acces_number[0],color_l[0])
card2 = create_card("Genre principal", acces_number[1],color_l[1])

card = dbc.Row([dbc.Col(id='card1', children=[card1], lg=3,width=6), dbc.Col(id='card2', children=[card2], lg=3,width=6)])
######################## Fin de création des cartes  ########################


######################## Création du dropdown ########################


radio_item=dcc.Dropdown(
   options=[
        {'label': i, 'value': i} for i in df_genres_propre.Genre.unique()
   ],
    searchable=False,
    id='dropdown-genre'
)

filtre_label =html.H2("Selectionne un genre : ",style={'color':'#ffff'})
filtre_line = dbc.Row([dbc.Col(filtre_label , lg=3,width=6), dbc.Col(radio_item, lg=6, width=6)])


######################## Fin du dropdown  ########################
######################## Création des visualisations  ########################

graph=dcc.Graph(id='genreTopGraph')
piegraph = dcc.Graph(id='genrePaysGraph')
graph_line =  dbc.Row([dbc.Col(graph, lg=8), dbc.Col(piegraph, lg=4)])

genreListeArtistes = html.Div(
        className="trend",
        children=[
            dbc.Alert("", color="info", id='propreGenre')

        ], )

######################## Footer  ########################
footer =dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Div('Auteurs : Nazir YOUSSOUF YAYE & Maureen METGE', className='mr-2',style={'color':'blue'}),
                    html.Div('Ynov Aix Campus : Projet B3', className='mr-2',style={'color':'blue'}),

                ],
                className='lead'
            )
        ,lg=12,
       )
    )

######################## Fin du footer  ########################

######################## Titre de la page et layout complet  ########################

elemTitre = html.H2("Genres", style={'color':'#ffff'})

layout_genres = html.Div([html.Br(),elemTitre, html.Br(),card, html.Br(), filtre_line,html.Br(), graph_line,html.Br(),genreListeArtistes,html.Br(),footer],style={"background-color":'black',"height": "100%", "min-height":"100vh","padding":"10px"})