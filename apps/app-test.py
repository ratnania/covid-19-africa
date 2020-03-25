# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq             as daq
from dash.dependencies import Output, Input, State

import plotly.graph_objs as go
import numpy as np
from pandas import read_csv

from utilities import load_country_map
from utilities import load_country_patients
from utilities import compute_barycenters
from utilities import plotly_country_map
from utilities import plotly_country_n_patients

# ...
COUNTRY = 'Morocco'
# ...

# ...
app = dash.Dash(__name__)
# ...

# ...
namespace = {}
namespace['contours'] = load_country_map(COUNTRY)
namespace['patients'] = load_country_patients(COUNTRY)
provinces = list(namespace['contours'].keys())

d_barycenters = compute_barycenters(namespace['contours'])
# ...

# =================================================================
app.layout = html.Div([
    html.H2('COVID-19'),
    #
    html.Div(className='Container', children=[
        html.Div(className='seven columns', children=[
            html.Div([dcc.Graph(id="graph")]),
        ]),
        #
        html.Div(className='four columns', children=[
            #
            html.Div([
                html.Label('Province'),
                dcc.Dropdown(id="province",
                             options=[{'label':name, 'value':name}
                                      for name in provinces],
                             value=[],
                             multi=True),
            ]),
        ]),
    ])
])

# =================================================================
@app.callback(
    Output("graph", "figure"),
    [Input("province", "value")]
)
def update_graph(provinces):
    traces = []

    # ...
    if 'contours' in list(namespace.keys()):
        d_contours = namespace['contours']
        for province, contour in d_contours.items():
            highlighted = province in provinces
            traces += plotly_country_map(province, contour,
                                         highlighted=highlighted)
    # ...

    # ...
    traces += plotly_country_n_patients(d_barycenters, namespace['patients'])
    # ...

    # ...
    showlegend = False
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
                        showlegend=showlegend,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                      )
    # ...

    return {'data': traces, 'layout': layout}


###########################################################
if __name__ == '__main__':

    app.run_server(debug=True)
