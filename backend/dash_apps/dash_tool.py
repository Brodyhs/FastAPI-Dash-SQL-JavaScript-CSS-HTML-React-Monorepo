import dash
from dash import dcc, html
import plotly.graph_objs as go

# Sample data
data = {
    'Fruits': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'Quantity': [5, 3, 8, 2]
}

# Create a Dash app
dash_app = dash.Dash(__name__, requests_pathname_prefix='/dash-tool/')

# Layout for the Dash app
dash_app.layout = html.Div(children=[
    html.H1('Fruit Quantities Bar Chart'),
    
    dcc.Graph(
        id='bar-chart',
        figure={
            'data': [
                go.Bar(
                    x=data['Fruits'],
                    y=data['Quantity'],
                    name='Fruits'
                )
            ],
            'layout': {
                'title': 'Fruit Quantities',
                'xaxis': {'title': 'Fruits'},
                'yaxis': {'title': 'Quantity'}
            }
        }
    )
])

# Run the Dash app
app = dash_app.server
