# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq             as daq
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go
import numpy as np
from pandas import read_csv
import yaml

# ...
COUNTRIES = ('Morocco',)
# ...

# ...
namespace = {}
# ...

# ...
app = dash.Dash('COVID-19')

text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)
# ...

# =================================================================
def plot_data(province, contour):

    x = contour[:,0]
    y = contour[:,1]

    line_marker = dict(width=2)

    trace_crv = go.Scatter(
        x=x,
        y=y,
        mode = 'lines',
        name=province,
        line=line_marker,
    )

    return [trace_crv]

# =================================================================
app.layout = html.Div([
    html.H2('COVID-19', style=text_style),
    #
    html.Div([
        html.Label('Country'),
        dcc.Dropdown(id="country",
                     options=[{'label':name, 'value':name}
                              for name in COUNTRIES],
                     value=[],
                     multi=False),
        #
        html.Button('load', id='button_load',
                    n_clicks_timestamp=0),
        dcc.Store(id='loaded_data'),
    ]),
    #
    html.Div([dcc.Graph(id="graph")]),
    ])

# =================================================================
@app.callback(
    Output("graph", "figure"),
    [Input("country", "value")]
)
def update_graph(country):

    if not isinstance(country, str):
        return {'data': []}

    traces = []

    # ...
    if 'contours' in list(namespace.keys()):
        d_contours = namespace['contours']
        for province, contour in d_contours.items():
            traces += plot_data(province, contour)
    # ...

    layout = go.Layout( xaxis=dict(showticklabels=False,
                                   showgrid=False,
                                   zeroline=False),
                        yaxis=dict(scaleanchor="x",
                                   scaleratio=1,
                                   autorange='reversed',
                                   showticklabels=False,
                                   showgrid=False,
                                   showline=False,
                                   zeroline=False),
                        showlegend=True )

    return {'data': traces, 'layout': layout}

# =================================================================
@app.callback(
    Output("loaded_data", "data"),
    [Input("country", "value"), Input('button_load', 'n_clicks_timestamp')]
)
def load_country(country, time_clicks):
    if not isinstance(country, str):
        return False

    # ... contours for a country
    fname = '../datasets/{country}/contours.yml'.format(country=country.lower())
    with open(fname) as f:
        d = yaml.load(f, Loader=yaml.Loader)
        d_contours = {}
        for k,v in d.items():
            x = np.array(v, dtype=int)
            y = x.reshape((len(x)//2,2))
            d_contours[k] = y

    namespace['contours'] = d_contours
    # ...

    return True


###########################################################
if __name__ == '__main__':

    app.run_server(debug=True)
