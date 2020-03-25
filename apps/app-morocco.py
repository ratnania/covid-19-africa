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
from utilities import plotly_country_map

# ...
COUNTRY = 'Morocco'
# ...

# ...
app = dash.Dash('COVID-19-{}'.format(COUNTRY))

text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)
# ...

namespace = load_country_map(COUNTRY)

# =================================================================
app.layout = html.Div([
    html.H2('COVID-19', style=text_style),
    #
    html.Div([
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
    [Input('button_load', 'n_clicks_timestamp')]
)
def update_graph(time_clicks):
    traces = []

    # ...
    if 'contours' in list(namespace.keys()):
        d_contours = namespace['contours']
        for province, contour in d_contours.items():
            traces += plotly_country_map(province, contour)
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


###########################################################
if __name__ == '__main__':

    app.run_server(debug=True)
