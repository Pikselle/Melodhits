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


################################bloc des cartes###########################
#courleurs des cartes
color_l=['info',"secondary",'info',"secondary","success","warning","danger"]
#fonctiond de création des cartes
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
#acces_number=df_pc.sum(axis=0)

acces_number = df_genres.sum(axis=0)

acces_number[0]= df_genres.Genre.unique().size
acces_number[1] = df_genres['Genre'].value_counts().idxmax()
acces_number[2]=df_genres.Pays.unique().size
acces_number[3] = df_genres['Pays'].value_counts().idxmax()

card1 = create_card("Nombre de genres différents", acces_number[0],color_l[0])
card2 = create_card("Genre principal", acces_number[1],color_l[1])

card = dbc.Row([dbc.Col(id='card1', children=[card1], lg=3,width=6), dbc.Col(id='card2', children=[card2], lg=3,width=6)])
#########################################Fin déclaration cartes######################################

##########@@###### bloc déclaration Pie graph###########################################
piegraph=dcc.Graph(id='pieGraph')
pie = dcc.Graph(
        id = "pieG",
        figure = {
          "data": [
            {
              "values": [800, 345, 500],
              "labels": [
                "Positive",
                "Negative",
                "Neutral"
              ],
              "name": "Sentiment",
              "hoverinfo":"label+name+percent",
              "hole": .7,
              "type": "pie"
              #"marker" : dict(colors['#05C7F2','#D90416','#D9CB04'])
}],
          "layout": {
                "title" : dict(text ="Sentiment Analysis",
                               font =dict(
                               size=20,
                               color = 'white')),
                "paper_bgcolor":"#111111",
                "width": "2000",
                "annotations": [
                    {
                        "font": {
                            "size": 20
                        },
                        "showarrow": False,
                        "text": "",
                        "x": 0.2,
                        "y": 0.2
                    }
                ],
                "showlegend": False
              }
        }
)

################################################# fin bloc déclaration Pigraph###########


##########################################bloc déclaration RadioItems###################
'''radio_item=dcc.RadioItems(
  options=[
      #{'label': 'choix date', 'value': 'choix'},
      {'label': '3 Mois', 'value': 'trois_mois'},
      {'label': '6 Mois', 'value': 'six_mois'},
      {'label': '1 An', 'value': 'un_an'},
      {'label': 'All', 'value': 'all'}

  ], #value='choix',
  labelStyle={'display': 'inline-block', 'width': '20%','color': '#ffff','marginTop': 13},
  id='radio-button-publishing'
  )'''

radio_item=dcc.Dropdown(
   options=[
        {'label': i, 'value': i} for i in df_genres_propre.Genre.unique()
   ],
    searchable=False,
    id='dropdown-genre'
)

filtre_label =html.H2("Selectionne un genre : ",style={'color':'#ffff'})
filtre_line = dbc.Row([dbc.Col(filtre_label , lg=3,width=6), dbc.Col(radio_item, lg=6, width=6)])

###################################Fin bloc déclaration RadioItems##################


#déclaration graph line et bar
graph=dcc.Graph(id='genreTopGraph')

#déclaration ligne entierre raph line , bar et pie graph#########
#graph_line = dbc.Row([dbc.Col(graph, lg=8), dbc.Col(piegraph, lg=4)])
piegraph = dcc.Graph(id='genrePaysGraph')
graph_line =  dbc.Row([dbc.Col(graph, lg=8), dbc.Col(piegraph, lg=4)])

genreListeArtistes = html.Div(
        className="trend",
        children=[
            dbc.Alert("", color="info", id='propreGenre')

        ], )

#déclaration footer#####@@@@@#################
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

elemTitre = html.H2("Genres", style={'color':'#ffff'})
#déclaration layout final
layout_genres = html.Div([html.Br(),elemTitre, html.Br(),card, html.Br(), filtre_line,html.Br(), graph_line,html.Br(),genreListeArtistes,html.Br(),footer],style={"background-color":'black',"height": "100%", "min-height":"100vh","padding":"10px"})