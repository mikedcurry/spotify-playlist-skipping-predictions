import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [   
        # dcc.Markdown(
        #     """
        
        #     ## Predicting The Perfect Playlist Recipe 


        #     """
        # ),
        html.Br(),
        html.Br(),
        html.Div('Without music,',style={'fontSize': 20, 'fontStyle': 'italic', 'paddingLeft':60}),
        html.Div('life would be a mistake.',style={'fontSize': 20, 'fontStyle': 'italic','paddingLeft':60}),
        html.Br(),
        html.Div('- Friedrich Nietzsche',style={'fontSize': 16,'paddingLeft':120}),
        html.Br(),
        html.Br(),
        html.Br(),
        
        html.Br(),
        dcc.Markdown(
            """
    

            By emphasizing the most definitive features of a track in Spotify's massive collection of playlists, we can learn what makes a Spotify playlist stand out.   

            Is it the steady electronic beat, the melody line, the overall loudness, or the clear vocals that keep us listening?     

            """
        ),
        html.Br(),
        dcc.Link(dbc.Button('Make a Prediction', color='success'), href='/predictions'), 
        html.Br(),
        html.Br(),
        html.Br(),

    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        # dcc.Graph(figure=fig),
        dcc.Markdown('''

        ![Scores](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/Homepage.png "Feature Dendrogram")
        '''

        ),
    ]
)

layout = dbc.Row([column1, column2])