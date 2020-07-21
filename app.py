import plotly.graph_objs as go
import numpy as np
import dash_auth
import dash
import dash_core_components as dcc
import dash_html_components as html

x = np.arange(0, 5, 0.1)
def f(x):
    return x**2
def h(x):
    return np.sin(x)

fig1 = go.Figure(go.Scatter(x=x, y=f(x)))
fig2 = go.Figure(go.Scatter(x=x, y=h(x)))

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css']

app = dash.Dash(external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    [('admin', 'secret')]
)

row0 = html.Div([html.Div([html.H1('Заголовок')], 
                          className='col-sm')],
                className='row')

row1 = html.Div([html.Div([dcc.Graph(figure=fig1)], 
                          className='col-sm'),
                 html.Div([dcc.Graph(figure=fig2)], 
                          className='col-sm')], 
                className='row')

row2 = html.Div([html.Div([html.P('f(x) = x<sup>2</sup>')], 
                          className='col-sm'),
                 html.Div([html.P('h(x) = sin(x)')], 
                          className='col-sm')], 
                className='row')

app.layout = html.Div([row0, row1, row2], 
                      className='container')




#app.run()
#if __name__ == '__main__':
app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter