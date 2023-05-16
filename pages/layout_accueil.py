from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from datetime import date, timedelta
from dash import dash_table
from datetime import datetime as dt



body = dbc.Container([
        html.Br(),
        dbc.Row(
                [
                dbc.Col(

                    html.Div(
                        [   html.Br([]),
                            html.H5("Bienvenue sur Melod'hits!",style={'color':'red','backgroundColor':'white'}),
                            html.Br([]),
                            html.P(
                                "\
                             Ceci est une plateforme qui permet de voir de nombreuses visualisations sur les genres de musique les plus populaires depuis les années 2000 !",

                                style={"color": "#000406"},

                            ),
                            html.P(
                                "\
                            Actuellement, il s'agit d'une première version qui comporte seulement les données des 100 musiques les plus écoutées de chaque année.\
                                Il y aura bientôt de nouvelles données avec de plus nombreux artistes, titres et genres !",


                                style={"color": "#000406"},

                            )
                        ]

                         )

                ,style={'color':'red','backgroundColor':'white'})
                    ], justify="center", align="center"
                    ),
],style={"height": "100vh"}
)

layout_accueil =  html.Div([body],style={'background-color': 'white'})
