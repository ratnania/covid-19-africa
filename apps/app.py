# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq             as daq
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go
import numpy as np

# ...
from utilities import update_dataset, clean_dataset
from utilities import read_deaths_cases
from utilities import read_confirmed_cases
from utilities import read_recovered_cases
from utilities import select_data_by_country
# ...

# ...
COUNTRIES = ('France', 'Italy', 'Germany', 'Tunisia', 'Morocco', 'Spain')
CASES = ('confirmed', 'deaths', 'recovered')
# ...

# ...
namespace = {}
# ...

# ...
app = dash.Dash('COVID-19')

text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)
# ...

# ...
def plot_data(country, case):
    # TODO do it oustside of plot_data
    name = '{country}-{case}'.format(country=country, case=case)

    try:
        df = namespace[case]

    except:
        raise ValueError('not available {}'.format(case))

    x,y = select_data_by_country(df, country)

    line_marker = dict(width=2)

    trace_crv = go.Scatter(
        x=x,
        y=y,
        mode = 'lines',
        name=name,
        line=line_marker,
    )

    return [trace_crv]
# ...

# =================================================================
app.layout = html.Div([
    html.H2('COVID-19', style=text_style),
    #
    html.Div([
        html.Button('update', id='button_update',
                    n_clicks_timestamp=0),
        dcc.Store(id='updated_data'),
        #
        html.Button('clean', id='button_clean',
                    n_clicks_timestamp=0),
        dcc.Store(id='cleaned_data'),
        #
        html.Button('load', id='button_load',
                    n_clicks_timestamp=0),
        dcc.Store(id='loaded_data'),
    ]),
    #
    html.Div([
        html.Label('Country'),
        dcc.Dropdown(id="country",
                     options=[{'label':name, 'value':name}
                              for name in COUNTRIES],
                     value=[],
                     multi=True),
    ]),
    #
    html.Div([
        html.Label('Case'),
        dcc.Dropdown(id="case",
                     options=[{'label':name, 'value':name}
                              for name in CASES],
                     value=[],
                     multi=True),
    ]),
    #
    html.Div([
        daq.BooleanSwitch(label='Log Scale',
          id='log_scale',
          on=False
        ),
    ]),
    #
    html.Div([dcc.Graph(id="graph")]),
    ])

# =================================================================
@app.callback(
    Output("graph", "figure"),
    [Input("country", "value"),
     Input("case", "value"),
     Input('log_scale', 'on')]
)
def update_graph(countries, cases, log_scale):

    if len(countries) == 0:
        return {'data': []}

    if len(cases) == 0:
        cases = ['confirmed']

    yaxis_type = 'linear'
    if log_scale:
        yaxis_type = 'log'

    traces = []
    for case in cases:
        for country in countries:
            traces += plot_data(country, case)

        layout = go.Layout( yaxis=dict(scaleanchor="x", scaleratio=1,
                                       type=yaxis_type),
                            showlegend=True )

    return {'data': traces, 'layout': layout}

# =================================================================
@app.callback(
    Output("cleaned_data", "data"),
    [Input('button_clean', 'n_clicks_timestamp')]
)
def clean_data(time_clicks):

    if time_clicks > 0 :
        clean_dataset()
        return True

    return False

# =================================================================
@app.callback(
    Output("updated_data", "data"),
    [Input('button_update', 'n_clicks_timestamp')]
)
def update_data(time_clicks):

    if time_clicks > 0 :
        update_dataset()
        return True

    return False

# =================================================================
@app.callback(
    Output("loaded_data", "data"),
    [Input('button_load', 'n_clicks_timestamp')]
)
def load_dataframe(time_clicks):

    try:
        namespace['confirmed'] = read_confirmed_cases()
        namespace['recovered'] = read_recovered_cases()
        namespace['deaths'] = read_deaths_cases()

        return True

    except:
        return False


###########################################################
if __name__ == '__main__':

    app.run_server(debug=True)
