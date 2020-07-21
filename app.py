import os

import plotly.graph_objs as go
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_auth

x = np.arange(0, 5, 0.1)
def f(x):
    return x**2
def h(x):
    return np.sin(x)

fig1 = go.Figure(go.Scatter(x=x, y=f(x)))
fig2 = go.Figure(go.Scatter(x=x, y=h(x)))

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)