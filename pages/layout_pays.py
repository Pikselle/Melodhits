from dash import dcc
from dash import html
from dash import dash_table
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import time
from components.functions import df_genres, df_pays
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
acces_number[0]=df_genres.Pays.unique().size
acces_number[1] = df_genres['Pays'].value_counts().idxmax()
payys = df_genres['Pays'].value_counts().idxmax()
sansdoublon = df_genres[['Artiste','Pays']].drop_duplicates()
sansdoublon = sansdoublon[sansdoublon['Pays'] == payys]
acces_number[2]= sansdoublon['Artiste'].value_counts().sum()
acces_number[3] = df_genres['Pays'].value_counts().idxmax()

card1 = create_card("Nombre de pays différents", acces_number[0],color_l[0])
card2 = create_card("Pays principal", acces_number[1],color_l[1])
card3 = create_card("Artistes du pays principal", acces_number[2],color_l[2])

card = dbc.Row([dbc.Col(id='card1', children=[card1], lg=3,width=6), dbc.Col(id='card2', children=[card2], lg=3,width=6), dbc.Col(id='card3', children=[card3], lg=3,width=6)])
######################## Fin de création des cartes  ########################


######################## Création du dropdown ########################

radio_item=dcc.Dropdown(
   options=[
        {'label': i, 'value': i} for i in df_pays.Pays.unique()
   ],
    searchable=True,
    id='dropdown-pays'
)

filtre_label =html.H2("Selectionne un pays : ",style={'color':'#ffff'})
filtre_line = dbc.Row([dbc.Col(filtre_label , lg=3,width=6), dbc.Col(radio_item, lg=6, width=6)])


######################## Fin du dropdown  ########################
######################## Création des visualisations  ########################

graph=dcc.Graph(id='paysTopGraph')

piegraph = dcc.Graph(id='paysGenreGraph')
graph_line =  dbc.Row([dbc.Col(graph, lg=8), dbc.Col(piegraph, lg=4)])

paysListeArtistes = html.Div(
        className="trend",
        children=[
            dbc.Alert("Artistes", color="info", id='proprePays')

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

elemTitre = html.H2("Pays", style={'color':'#ffff'})

layout_pays = html.Div([html.Br(),elemTitre, html.Br(),card, html.Br(), filtre_line,html.Br(), graph_line,html.Br(),paysListeArtistes,html.Br(),footer],style={"background-color":'black',"height": "100%", "min-height":"100vh","padding":"10px"})