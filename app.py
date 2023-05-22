import dash
import dash_bootstrap_components as dbc

bootstrap_theme = [dbc.themes.BOOTSTRAP, 'https://use.fontawesome.com/releases/v5.9.0/css/all.css']
app = dash.Dash(__name__, external_stylesheets=bootstrap_theme)
app.title = 'Melodhit'
app._favicon = ("Logo-melodhit-noir.png")
server = app.server
app.config.suppress_callback_exceptions = True