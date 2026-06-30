import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

# Register this page
dash.register_page(__name__, path='/', name='Home')

# Page layout
def layout():
    return html.Div([
        # Main content container - centered and 80% width
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    # Welcome card
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Markdown(
                                """## Welcome to the Binary Choice Study! 🏡

### About this example
This is a demonstration of a binary choice experiment designed with PixelSurvey. Our example develop a binary choice experiment with two alternatives, where one attirbute is an image and the other is a standard numeric attribute. The experiment is based on a custom design located in the `assets/exp1/sc_custom_design.csv`.

### Survey structure
- Homepage (this page)
- Informed Consent
- Participant Screening (three questions)
- An Binary Choice Experiment activity with 8 choice tasks  
- A questionnaire with 4 questions about housing preferences and habits
- Thank you page

### How to start building your own survey
1. I suggest modifying the content of this survey to be familiar with the structure and YAML format.
2. Then, you can start building your own survey by changing the content and structure.
3. Remember that PixelSurvey just read an experiment design file, so you can create your own custom design with any software (e.g., Ngene, Excel, etc.) and upload it to the `assets` folder. Then, you just need to specify the path to your custom design in the `custom_design` field of the experiment activity.

I hope this example helps you to get started with PixelSurvey and to design your own experiments and surveys. If you have any questions or need further assistance, feel free to reach out!
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
                            "Start Survey",
                            id="home-button",
                            color="primary",
                            size="lg",
                            href="/consent#top",
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
