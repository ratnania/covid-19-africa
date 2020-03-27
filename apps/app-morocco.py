# -*- coding: utf-8 -*-
# TODO share data between callbacks: see  https://dash.plotly.com/sharing-data-between-callbacks
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq             as daq
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

import plotly.graph_objs as go
import numpy as np
from pandas import read_csv
import pandas as pd
from datetime import datetime as dt
import datetime

from utilities import load_country_map
from utilities import load_country_patients
from utilities import compute_barycenters
from utilities import plotly_country_map
from utilities import plotly_country_n_patients
from utilities import select_by_date

# ...
COUNTRY = 'Morocco'
# ...

# ...
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'COVID-19 Morocco'

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF',
    #'background-body': '#ffe6e6'
    'background-body':'#b3ccff'
}
# ...

# ...
namespace = {}
namespace['contours'] = load_country_map(COUNTRY)
namespace['patients'] = load_country_patients(COUNTRY)

provinces = list(namespace['contours'].keys())

d_barycenters = compute_barycenters(namespace['contours'])
# ...

# =================================================================

app.layout = html.Div(style={'backgroundColor': colors['background-body'], 'max-width': '100%', 'overflow-x': 'hidden'}, children=
    [
        #=========================== HEADER ======================
        dbc.Row(
            [
                dbc.Col(html.Div(
                    html.Img(src='./assets/images/um6p-logo.png', style={'height':'50%', 'width':'50%', 'align':'center'})
                ,className="ml-2"), className="col-md-4 col-sm-12 ml-10"),
                dbc.Col(html.Div(
                    html.H4("Covid-19 Morocco", style={'color':'#22549F', 'align':'center'})
                ), className="col-md-4  col-sm-12"),
                dbc.Col(html.Div(children=[
                    html.P(children=["Mohammed VI Polytechnic university", html.Br(),"Modeling, Simulation and Data Analysis"], style={'color':'#22549F', 'align':'center'}),
                ]), className="col-md-4  col-sm-12"),  
            ], justify="center", align="center", className="h-50", style={'backgroundColor': colors['background']}
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(
                    html.Hr()
                ), className="col-md-12") 
            ], style={'backgroundColor': colors['background']}
        ),
        #=========================== BODY ======================
        dbc.Row(
            [
                dbc.Col(
                    html.Div(className='', children=[
                        html.Div([dcc.Graph(id="map")]),
                    ]), className="col-md-8"
                ),
                dbc.Col(
                    html.Div(children=[
                    html.Div(children=[
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
                                        end_date=datetime.date.today()),
    #                                    end_date_placeholder_text='Select a date!',
                        ])
                    ])
                ]), className="col-md-4 text-center mt-5 border rounded border-primary")  
            ], className="mr-2"  
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(
                    html.Div([
                html.Div([dcc.Graph(id="graph")]),
                ])), className="col-md-6"),
                dbc.Col(html.Div(
                    html.Div([
                html.Div([html.P('TODO Another Graph')]),
                ])), className="col-md-6"),
            ], 
        ),
   
         dbc.Row(
            [
                dbc.Col(html.Div(
                    html.Hr()
            ), className="col-md-12"),
                
            ], style={'backgroundColor': colors['background']} 
        ),
        #=========================== FOOTER ======================
         dbc.Row(
            [
                dbc.Col(html.Div(
                    html.P('Copyright MSDA © 2020. All rights reserved.', style={'color':'#22549F', 'align':'center'})
                ), className="col-md-12 text-center"),
            ], style={'backgroundColor': colors['background']}
        )
    ])

# =================================================================
@app.callback(
    Output("map", "figure"),
    [Input("province", "value"),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_map(provinces, start_date, end_date):

    # ...
    # TODO we should use dash storage
    date_key = 'confirmed_date'

    df = select_by_date(namespace['patients'], date_key, start_date, end_date)
    # ...

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
    traces += plotly_country_n_patients(d_barycenters, df)
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

# =================================================================
@app.callback(
    Output("graph", "figure"),
    [Input("province", "value"),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_graph(provinces, start_date, end_date):

    traces = []

    # ...
    layout = go.Layout( xaxis=dict(showticklabels=True,
                                   showgrid=False,
                                   zeroline=False),
                        yaxis=dict(scaleanchor="x",
                                   scaleratio=1,
                                   showticklabels=True,
                                   showgrid=True,
                                   showline=True,
                                   zeroline=True),
                        showlegend=True,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                      )
    # ...

    if len(provinces) == 0:
        return {'data': traces, 'layout': layout}

    # ...
    # TODO we should use dash storage
    date_key = 'confirmed_date'

    df = select_by_date(namespace['patients'], date_key, start_date, end_date)
    # ...

    # ...
    df0 =  pd.DataFrame([0, 0], index=pd.to_datetime([start_date, end_date]))

    for province in provinces:
        _df = df[df['province'] == province]

        dt_series = _df[date_key].value_counts()
        dt_series = dt_series.append(df0)

        dt_series.sort_index(inplace=True)
        dt_series = dt_series.asfreq('D')
        dt_series = dt_series.fillna(0)
        dt_series = dt_series.cumsum()

        dates = dt_series.axes[0]
        days = dates.day
        months = dates.month
        dates = ['{d}/{m}'.format(d=d, m=m) for d,m in zip(days, months)]

        values = dt_series.values[:,0]

        line_marker = dict(width=2)

        trace = go.Scatter(
            x=dates,
            y=values,
            mode = 'lines',
            name=province,
            line=line_marker,
        )

        traces.append(trace)
    # ...

    return {'data': traces, 'layout': layout}



###########################################################
if __name__ == '__main__':

    app.run_server(debug=True)
