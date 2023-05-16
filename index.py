from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import callbacks
from pages.header import navbar
from pages.layout_dashboard import layout_dashboard
from pages.layout_accueil import layout_accueil
from pages.layout_artistes import layout_artistes
from pages.layout_emotions import layout_emotions
from pages.layout_genres import layout_genres
from pages.layout_pays import layout_pays
from app import app,server


# Layout rendu par l'application
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    navbar,
    html.Div(id='page-content')
])

# Callback de routage
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname=='/accueil' or pathname=='/':
        return layout_accueil
    elif pathname=='/top100':
        return layout_dashboard,
    elif pathname=='/artistes':
        return layout_artistes,
    elif pathname=='/pays':
        return layout_pays,
    elif pathname=='/genres':
        return layout_genres,
    elif pathname=='/emotions':
        return layout_emotions,


if __name__ == '__main__':
    app.run_server(debug=True)
