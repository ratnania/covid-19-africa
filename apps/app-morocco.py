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
from utilities import load_country_statistics_age
from utilities import load_country_statistics_gender
from utilities import compute_barycenters
from utilities import plotly_country_map
from utilities import plotly_country_n_patients
from utilities import select_by_date

# ...
COUNTRY = 'Morocco'
# ...

# ...
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.title = 'COVID-19 Morocco'

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF',
    'background-body':'#b3ccff'
}

layoutEmpty = go.Layout( xaxis=dict(showticklabels=False,
                                   showgrid=False,
                                   zeroline=False),
                        yaxis=dict(scaleanchor="x",
                                   scaleratio=1,
                                   showticklabels=False,
                                   showgrid=False,
                                   showline=False,
                                   zeroline=False),
                        showlegend=False,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)'
                      )
# ...

# ...
namespace = {}
namespace['contours'] = load_country_map(COUNTRY)
namespace['patients'] = load_country_patients(COUNTRY)
namespace['statistics_age'] = load_country_statistics_age(COUNTRY)
namespace['statistics_gender'] = load_country_statistics_gender(COUNTRY)

provinces = list(namespace['contours'].keys())


d_barycenters = compute_barycenters(namespace['contours'])
# ...

# =================================================================

app.layout = html.Div(style={'backgroundColor': colors['background-body'], 'max-width': '100%', 'overflow-x': 'hidden'}, children=
    [
        #=========================== HEADER ======================
        dbc.Row(
            [
                html.Div(html.Div(
                    html.Img(src='./assets/images/um6p-logo.png', style={'height':'50%', 'width':'50%'})), className="col-md-4  text-center"),
                html.Div(html.Div(
                    html.H4("Covid-19 Morocco", style={'color':'#22549F'})
                ), className="col-md-4 text-center"),
                html.Div(html.Div(children=[
                    html.P(children=["Mohammed VI Polytechnic university", html.Br(),"Modeling, Simulation and Data Analysis"], style={'color':'#22549F', 'align':'center'}),
                ]), className="col-md-4 text-center"),  
            ], justify="center", align="center", className="h-50", style={'backgroundColor': colors['background']}
        ),
        #=========================== BODY ======================
        dbc.Row(
            [
                dbc.Col(
                    html.Div(className='twelve columns', children=[
                        html.Div([dcc.Graph(id="map")]),
                    ]), className="col-md-8"
                ),
                dbc.Col(
                    html.Div(children=[
                    html.Div(children=[
                        html.Div([
                            html.Hr(),
                            html.H6(' Search ', style={'color':'#22549F'}),
                            html.Hr(),
                            html.P('please choose search criteria below to display the graphs'),
                            html.Hr()
                        ]),
                        html.Div([
                            html.Label('Province'),
                            dcc.Dropdown(id="province",
                                options=[{'label':name, 'value':name}
                                        for name in provinces],
                                value=[],
                                multi=True),
                        ]),
                        html.Hr(),
                        html.Label('Period'),
                        html.Div([
                            dcc.DatePickerRange(id='date-picker-range',
                                        start_date=dt(2020, 3, 2),
                                        end_date=datetime.date.today()),
    #                                    end_date_placeholder_text='Select a date!',
                        ]),
                        html.Hr(),
                        html.Label('Other criteria'),
                        html.Div([
                           dbc.Checklist(id="criteria",
                                options=[
                                    {'label': 'Age', 'value': 'age'},
                                    {'label': 'Gender', 'value': 'gender'}
                                ],
                                value=['age', 'gender'],
                                inline=True)
                        ]),
                        html.Hr(),
                        html.Div([
                            html.P(['Last update: ', html.B(id="updatedAt", className='text-danger')])
                        ]),
                    ])
                ]), className="col-md-4 text-center mt-5 border rounded border-primary")  
            ], className="ml-2 mr-2"  
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(
                    html.Div([
                html.Div([dcc.Graph(id="graph")]),
                ])), className="col-md-12")
            ], 
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(id="gender-container",children=[
                    html.Div([
                 html.Div([dcc.Graph(id="pieChartGender")]),
                ])]), className="col-md-6"),
                dbc.Col(html.Div(id="age-container",children=[
                    html.Div([
                 html.Div([dcc.Graph(id="pieChartAge")]),
                ])]), className="col-md-6"),
            ], 
        ),
        #=========================== FOOTER ======================
         dbc.Row(
            [
                dbc.Col(html.Div(
                    html.P(['Copyright ',html.A('MSDA', href='https://msda.um6p.ma', target='_blank'), ' © 2020. All rights reserved.'], style={'color':'#22549F', 'align':'center'})
                ), className="col-md-12 text-center"),
            ], style={'backgroundColor': colors['background']}
        )
    ])

# =================================================================
@app.callback(
    Output('gender-container', 'style'),
    [Input('criteria','value')]
)
def hideGraphGender(input):
    if 'gender' in input:
        return {'display':'block'}
    else:
        return {'display':'none'}

# =================================================================
@app.callback(
    Output('age-container', 'style'),
    [Input('criteria','value')]
)
def hideGraphAge(input):
    if 'age' in input:
        return {'display':'block'}
    else:
        return {'display':'none'}

# =================================================================
@app.callback(
    Output('updatedAt', 'children'),
     [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]

)
def updatedAt(start_date, end_date):
    date_key = 'confirmed_date'
    df = select_by_date(namespace['patients'], date_key, start_date, end_date)
    return list(df[date_key])[-1].strftime('%d-%m-%Y')

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
                        title="Distribution of cases by province",
                        height=650  # px
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
                        title="Evolution of COVID-19"
                      )
    # ...

    if len(provinces) == 0:
        return {'data': traces, 'layout': layoutEmpty}

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
        dt_series = dt_series[~dt_series.index.duplicated()]
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

# =================================================================
@app.callback(
    Output("pieChartGender", "figure"),
    [Input("province", "value"),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input("criteria", "value")]
)
def update_pieChartGender(provinces, start_date, end_date, criteria):

    piedata = []
    labels = []
    values = []
    layout = {
        "title": {
            "text": "Distribution of cases by gender"
        },
        "xaxis": dict(showticklabels=False,
                    showgrid=False,
                    zeroline=False),
        "yaxis": dict(scaleanchor="x",
                    scaleratio=1,
                    showticklabels=False,
                    showgrid=False,
                    showline=False,
                    zeroline=False),
        "paper_bgcolor": 'rgba(0,0,0,0)',
        "plot_bgcolor": 'rgba(0,0,0,0)',
        "legend": {
            "x": 1.037488076311606,
            "y": 1,
            "title": {
                "text": "Gender"
            },
            "traceorder": "reversed",
            "bordercolor": "rgb(68, 68, 68)",
            "borderwidth": 1,
            "orientation": "v"
        },
    }
    
    if len(provinces) == 0:
        return {'data': piedata, 'layout': layoutEmpty}
    if 'gender' not in criteria:
        return {'data': piedata, 'layout': layoutEmpty}

    # ...
    date_key = 'confirmed_date'

    df = select_by_date(namespace['patients'], date_key, start_date, end_date)
    
    for province in provinces:
        _df = df[df['province'] == province]
        # Construct labels and values of pie: 
        for sex in _df['sex']:
            labels.append(sex)
        for x in range(0, len(_df)):
	        values.append('1')        
       
    # ...
    # Check if all lines has value of gender value
    for i in set(labels):
        if i not in ['male', 'female']:
            # we can get statistics from file statics_gender because we have some empty lines in the main file:
            dfGender = namespace['statistics_gender']
            labels = []
            values = []
            nbrMale = int(dfGender[dfGender['cle'] == 'male']['valeur'])
            nbrFemale = int(dfGender[dfGender['cle'] == 'female']['valeur'])
            for line in range(0, nbrMale):
                labels.append('male')
                values.append('1')
            for line in range(0, nbrFemale):
                labels.append('female')
                values.append('1')

    piedata = go.Pie(
            labels = labels,
            values = values,
            hoverinfo = 'label+value+percent', textinfo='value',
            domain = {"column": 0},
            #title = "gender",
            hole = .4,
            type = "pie"
    )

    return {'data': [piedata],'layout': layout}

# =================================================================
@app.callback(
    Output("pieChartAge", "figure"),
    [Input("province", "value"),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input("criteria", "value")]

)
def update_pieChartAge(provinces, start_date, end_date, criteria):

    piedata = []
    labels = []
    values = []
    layout = {
        "title": {
            "text": "Distribution of cases by age"
        },
        "xaxis": dict(showticklabels=False,
                    showgrid=False,
                    zeroline=False),
        "yaxis": dict(scaleanchor="x",
                    scaleratio=1,
                    showticklabels=False,
                    showgrid=False,
                    showline=False,
                    zeroline=False),
        "paper_bgcolor": 'rgba(0,0,0,0)',
        "plot_bgcolor": 'rgba(0,0,0,0)',
        "legend": {
            "x": 1.037488076311606,
            "y": 1,
            "title": {
                "text": "Age:"
            },
            "traceorder": "reversed",
            "bordercolor": "rgb(68, 68, 68)",
            "borderwidth": 1,
            "orientation": "v"
        },
    }
    
    if len(provinces) == 0:
        return {'data': piedata, 'layout': layoutEmpty}
    if 'age' not in criteria:
        return {'data': piedata, 'layout': layoutEmpty}
    
    date_key = 'confirmed_date'

    df = select_by_date(namespace['patients'], date_key, start_date, end_date)
   
    for province in provinces:
        _df = df[df['province'] == province]
        
        # Construct labels and values of pie:
        for age in _df['age']:
            if age <= 5 :
                labels.append('[00 - 05] YEARS')
            if age <= 15 :
                labels.append('[06 - 15] YEARS')
            elif age <= 25 :
                labels.append('[16 - 25] YEARS')
            elif age <= 40 :
                labels.append('[26 - 40] YEARS')
            elif age <= 65 :
                labels.append('[41 - 65] YEARS')
            elif age > 65 :
                labels.append('> 65  YEARS')
            else :
                labels.append('OTHERS')
        for x in range(0, len(_df)):
	        values.append('1')        
       
    # ...
    # Check if all lines has value of gender value
    for i in set(labels):
        if i == 'OTHERS':
            # we can get statistics from file statics_gender because we have some empty lines in the main file:
            dfAge = namespace['statistics_age']
            if len(dfAge['cle']) != 0 :
                labels = []
                values = []
                # Count elements by keys:
                _0_5 = int(dfAge[dfAge['cle'] == '[00 - 05] YEARS']['valeur'])
                _6_15 = int(dfAge[dfAge['cle'] == '[06 - 15] YEARS']['valeur'])
                _16_25 = int(dfAge[dfAge['cle'] == '[16 - 25] YEARS']['valeur'])
                _26_40 = int(dfAge[dfAge['cle'] == '[26 - 40] YEARS']['valeur'])
                _41_65 = int(dfAge[dfAge['cle'] == '[41 - 65] YEARS']['valeur'])
                _sup_65 = int(dfAge[dfAge['cle'] == '> 65 YEARS']['valeur'])

                for line in range(0, _0_5):
                    labels.append('[00, 05] YEARS')
                    values.append('1')
                for line in range(0, _6_15):
                    labels.append('[06, 15] YEARS')
                    values.append('1')
                for line in range(0, _16_25):
                    labels.append('[16, 25] YEARS')
                    values.append('1')
                for line in range(0, _26_40):
                    labels.append('[26, 40] YEARS')
                    values.append('1')
                for line in range(0, _41_65):
                    labels.append('[41, 65] YEARS')
                    values.append('1')
                for line in range(0, _sup_65):
                    labels.append('> 65  YEARS')
                    values.append('1')

    piedata = go.Pie(
            labels = labels,
            values = values,
            hoverinfo = 'label+value+percent', textinfo='value',
            domain = {"column": 0},
            #title = "Evolution by Age",
            type = "pie"
    )
    
    return {'data': [piedata],'layout': layout}

###########################################################
if __name__ == '__main__':

    app.run_server(debug=True)
