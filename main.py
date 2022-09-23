# Run this app with `python main.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import ast
import base64
import io

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State, MATCH, ALL

from tribedash.last14 import last14_layout

sign_out = dbc.NavItem(dbc.NavLink("Sign out", href="#"))
scrims15 = dbc.NavItem(dbc.NavLink("Your Profile", href="/scrims15"))
KCORP_LOGO = "https://i.imgur.com/dg8mqua.png"

# this example that adds a logo to the navbar brand
logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Savvy", className="ms-2")),
                    ],
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [scrims15, sign_out],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="dark",
    dark=True,
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://use.fontawesome.com/releases/v6.1.1/css/all.css',
                                      'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css'],
                suppress_callback_exceptions=True)
server=app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='team-to-load', storage_type='local'),
    html.Div(id="test-store"),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    return html.Div([logo, last14_layout])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=False, port=8081)
