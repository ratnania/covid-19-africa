# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq             as daq
from dash.dependencies import Output, Input, State
from datetime import datetime as dt

import plotly.graph_objs as go
import numpy as np
from pandas import read_csv
import pandas as pd

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
            html.Label('Period'),
            html.Div([
                dcc.DatePickerRange(id='date-picker-range',
                                    start_date=dt(2020, 3, 2),
                                    end_date_placeholder_text='Select a date!'),
                html.Div(id='output-container-date-picker-range')
            ]),
        ]),
    ])
])

# =================================================================
@app.callback(
    Output('output-container-date-picker-range', 'children'),
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')])
def update_output(start_date, end_date):

    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date = dt.strptime(start_date.split('T')[0], '%Y-%m-%d')
        start_date_string = start_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '

    if end_date is not None:
        end_date = dt.strptime(end_date.split('T')[0], '%Y-%m-%d')
        end_date_string = end_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string

    DATE_KEY = 'confirmed_date'
    df = namespace['patients']
    df[DATE_KEY] = pd.to_datetime(df[DATE_KEY])

    mask = True
    if start_date is not None:
        mask = mask & (df[DATE_KEY] > start_date)

    if end_date is not None:
        mask = mask & (df[DATE_KEY] <= end_date)

    df = df.loc[mask]
    print(df)

    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix

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
