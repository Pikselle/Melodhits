import dash
import dash_bootstrap_components as dbc
from dash import html

LOGO = "../assets/Melodhits-logo.png"

elem = dbc.Navbar(
    [
        html.A(dbc.Row(
            [   #logo
                dbc.Col(html.Img(src=LOGO, height="40px")),
                dbc.Col(dbc.NavbarBrand("Melod'hits", className="ms-2")),
                ]
        ))],
    color="dark",
    dark=True,)

navbar = dbc.Navbar(
    [
        html.A(
            # Alignement vertical de l'image et de l'acceuil
            dbc.Row(
                [
                    elem,
                    #Navlink Acceuil
                    dbc.Col(dbc.NavLink("Accueil", href="/accueil",style={'color':'white'})),
                    #Navlink dashbord
                    dbc.Col(dbc.NavLink("Evolution", href="/top100",style={'color':'white'})),
                    dbc.Col(dbc.NavLink("Artistes", href="/artistes",style={'color':'white'})),
                    dbc.Col(dbc.NavLink("Pays", href="/pays", style={'color': 'white'})),
                    dbc.Col(dbc.NavLink("Genres", href="/genres",style={'color':'white'})),
                    dbc.Col(dbc.NavLink("Emotions", href="/emotions",style={'color':'white'})),
                ],
                align="center",
                className="g-0",
                style={"padding-left":"10px"}
            ),
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
    ],
    color="dark",
    dark=True,
)