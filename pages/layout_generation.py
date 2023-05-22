from dash import dcc
from dash import html
from dash import dash_table
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import time
from components.functions import df_genres
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

######################## Fonctions de créations des KPI  ########################

# Couleurs des KPI
color_l=['info',"secondary",'info',"secondary","success","warning","danger"]

'''ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)'''
ALLOWED_TYPES = (
    "text", "number"
)

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
acces_number[0]=df_genres.Genre.unique().size
acces_number[1] = df_genres['Genre'].value_counts().idxmax()
acces_number[2]=df_genres.Pays.unique().size
acces_number[3] = df_genres['Pays'].value_counts().idxmax()

card1 = create_card("Nombre de genres différents", acces_number[0],color_l[0])
card2 = create_card("Genre principal", acces_number[1],color_l[1])
card3 = create_card("Nombre de pays différents", acces_number[2],color_l[2])
card4 = create_card("Pays principal", acces_number[3],color_l[3])

card = dbc.Row([dbc.Col(id='card1', children=[card1], lg=3,width=6), dbc.Col(id='card2', children=[card2], lg=3,width=6), dbc.Col(id='card3', children=[card3], lg=3,width=6), dbc.Col(id='card4', children=[card4], lg=3,width=6)])
######################## Fin de création des cartes  ########################

######################## Création du dropdown ########################

radio_item=dcc.Dropdown(
   options=[
        {'label': i, 'value': i} for i in df_genres.Annee.unique()
   ],
    searchable=False,
    id='dropdown-publishing'
)

input_item = dcc.Input(
            id="input_word",
            placeholder="Choisis le thème",
        )

filtre_label =html.H2("Choisis le thème : ",style={'color':'#ffff'})
filtre_line = dbc.Row([dbc.Col(filtre_label , lg=3,width=6), dbc.Col(input_item, lg=6, width=6)])


######################## Fin du dropdown  ########################
######################## Création des visualisations  ########################

graph=dcc.Graph(id='paroles')
piegraph = dcc.Graph(id='paysGraph')
graph_line =  dbc.Row([dbc.Col(graph, lg=8), dbc.Col(piegraph, lg=4)])

ParolesGenerees = html.Div(
        className="trend",
        children=[
            dbc.Alert("", color="info", id='paroles')

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

elemTitre = html.H2("Emotions", style={'color':'#ffff'})

elemConstruction = html.Div("PAGE EN CONSTRUCTION", style={"font-size":"32px", "color" : "white", "margin-bottom":"100px"})
#layout_emotions = html.Div([html.Br(),elemTitre, html.Br(),card, html.Br(), filtre_line,html.Br(), graph_line,html.Br(),footer],style={"background-color":'black',"height": "100%", "min-height":"100vh","padding":"10px"})
layout_generation = html.Div([html.Br(),elemTitre, html.Br(),filtre_line,html.Br(), ParolesGenerees,html.Br(),footer],style={"background-color":'black',"height": "100%", "min-height":"100vh","padding":"10px"})