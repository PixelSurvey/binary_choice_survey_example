import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
import time
from database import Database

# Database
db = Database('database.db')

# Register this page
dash.register_page(__name__, path='/instructions', name='Instructions')

# Page layout
def layout():
    return html.Div([
        # Main content container - centered and 80% width
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    # Instructions card
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Markdown(
                                """## Study Instructions

You will now complete 1 **Binary Choice** activity related to housing preferences. Then, you have to replied some questions related to your housing preferences. Please read the instructions carefully for each section.

For the activity you have to imagine that you are in the market for a new home and you are evaluating different properties based on their characteristics. In each choice task, you will be presented with two properties and you will have to choose which one you prefer based on the information provided. The properties will be described by an image and a price.
""",
                                style={
                                    "fontSize": "16px",
                                    "lineHeight": "1.6",
                                    "color": "#333",
                                    "textAlign": "justify"
                                }
                            )
                        ], style={"padding": "2rem"})
                    ], style={
                        "boxShadow": "0 4px 8px rgba(0,0,0,0.1)",
                        "borderRadius": "12px",
                        "border": "none",
                        "marginTop": "2rem",
                        "marginBottom": "2rem"
                    }),
                    
                    # Begin button - centered below the card
                    html.Div([
                        dbc.Button(
                            "Begin Activities",
                            id="instructions-button",
                            color="primary",
                            size="lg",
                            href="/act1/1#top",
                            style={
                                "fontSize": "18px",
                                "fontWeight": "bold",
                                "padding": "12px 40px",
                                "borderRadius": "8px",
                                "boxShadow": "0 2px 4px rgba(0,0,0,0.2)"
                            }
                        )
                    ], style={
                        "textAlign": "center",
                        "marginBottom": "3rem"
                    })
                    
                ], width={"size": 10, "offset": 1})  # 80% width (10/12) with 1 column offset on each side
            ])
        ], fluid=True, style={"minHeight": "80vh", "backgroundColor": "#f8f9fa"})  # Light gray background
    ])


# Callback to handle instructions button click - register time in database
@callback(
    Output('instructions-button', 'n_clicks'),
    Input('instructions-button', 'n_clicks'),
    State('user-store', 'data'),
    prevent_initial_call=True
)
def handle_instructions_click(n_clicks, user_data):
    if n_clicks and user_data:
        # Register time in database
        db.register_time(user_data['id'], 'instructions-button', time.time())
    
    return n_clicks
