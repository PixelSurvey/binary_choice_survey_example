import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from dash import get_relative_path as asset
from pathlib import Path

# Dash survey app and server
app = dash.Dash(__name__, 
				external_stylesheets = [dbc.themes.BOOTSTRAP], 
				use_pages = True,
				suppress_callback_exceptions = True)
server = app.server
survey_color = "#2E8B57"

def header():
    user_logo_url = "/" + Path(r"assets/logos/user_logo.png").as_posix()
    ps_logo_url = "/" + Path(r"assets/logos/pixelsurvey_logo.png").as_posix()
    left_logo = html.Img(src = asset(user_logo_url), className = "my-3 img-fluid", style = {"maxHeight": "60px", "objectFit": "contain"})
    right_logo = html.Img(src = asset(ps_logo_url), className = "my-3 img-fluid", style = {"maxHeight": "60px", "objectFit": "contain"})
    title = html.H1("Binary Choice for House Preferences", style = {"fontSize": "clamp(18px, 5vw, 30px)", "color":"white", "marginBottom": "0.2rem"})
    subtitle = html.H6("A study on consumer preferences for residential properties", style = {"fontSize": "clamp(12px, 3vw, 20px)", "color":"white", "marginBottom": "0"}, className = "lead")

    return html.Div(
        children = [ 
            dbc.Row( 
                children  = [
                    dbc.Col(left_logo, xs=3, md=2, align = "center", style = {"textAlign": "left", "paddingLeft": "2%"}),
                    dbc.Col([title, subtitle], xs=6, md=8, align="center", style = {"textAlign": "center", "padding": "0"}),
                    dbc.Col(right_logo, xs=3, md=2, align="center", style = {"textAlign": "right", "paddingRight": "2%"})],
                className="g-0 align-items-center"
            )],
        className = "py-1", style = {"backgroundColor": survey_color})


def footer():
    return html.Div([
        html.Hr(style={"margin": "0.5rem 0", "border": "1px solid #e0e0e0"}),
        html.Div([
            html.P([
                "Survey ID: ",
                html.Strong("binary_choice_example", style={"color": survey_color}),
                " | Generated with ",
                html.Strong("PixelSurvey (Albatros) 1.0", style={"color": survey_color}),
            ], style={"margin": "0.3rem 0", "fontSize": "14px", "color": "#666"}),
            html.P([
                "PixelSurvey® is a registered trademark © 2025. All rights reserved."
            ], style={"margin": "0.3rem 0", "fontSize": "12px", "color": "#888"}),
        ], style={"textAlign": "center", "padding": "0.5rem 0"})
    ])


app.layout = html.Div([
    # Global top anchor for all pages
    html.Div(id="top", style={"position": "absolute", "top": "0"}),
    dcc.Store(id = "user-store", data = {"id": -1, "tasks": None}, storage_type = "session"),
    dcc.Store(id = "hrefs-store", data = {"next": None}, storage_type = "session"),
	dcc.Store(id = "external-user", data = {"id": -1}, storage_type = "session"),
    dcc.Store(id = "last_task_resp_act1", data = {"task": None}, storage_type = "session"),
    dcc.Location(id = "url", refresh = False),
    header(),
    dash.page_container,
    html.Hr(),
    footer()
])


if __name__ == "__main__":
	app.run(debug = True)