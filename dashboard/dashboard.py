import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Curing Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='''
        Metrics for monitoring and optimizing your food experience...
    ''', style={
            'textAlign': 'center',
            'color': colors['text']
        }),


    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['humidity', 'temperature', 'fluctuation'], 'y': [4, 1, 2], 'type': 'bar',
                    'name': 'Bacon 1. try [weeks 2-4]'},
                {'x': ['humidity', 'temperature', 'fluctuation'], 'y': [2, 4, 5],
                    'type': 'bar', 'name': u'Bacon 2. try [weeks 4-6]'},
            ],
            'layout': {
                'title': 'Factor analysis - adjustable variables for curing fridge'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
