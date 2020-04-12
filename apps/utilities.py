from dataflows import Flow, load, dump_to_path, dump_to_zip, printer
from dataflows import add_metadata, checkpoint
from dataflows import sort_rows, filter_rows, find_replace, delete_fields, set_type, validate, unpivot

import shutil
import os

import numpy as np
from pandas import read_csv
from datetime import datetime as dt
import pandas as pd
import yaml

import plotly.graph_objs as go

# *******************************************************************
# Load data utilities
# *******************************************************************
BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
CONFIRMED = 'time_series_19-covid-Confirmed.csv'
DEATH = 'time_series_19-covid-Deaths.csv'
RECOVERED = 'time_series_19-covid-Recovered.csv'

def update_dataset():
    flow = Flow(
        # Load inputs
        load(f'{BASE_URL}{CONFIRMED}'),
        load(f'{BASE_URL}{RECOVERED}'),
        load(f'{BASE_URL}{DEATH}'),
        checkpoint('load_data'),
        # Process them (if necessary)
        # Save the results
        add_metadata(name='csse_covid_19_time_series', title='''csse_covid_19_time_series'''),
        printer(),
        dump_to_path(),
    )
    flow.process()

def clean_dataset():
    for name in ('Confirmed', 'Deaths', 'Recovered'):
        fname = 'time_series_19-covid-{}.csv'.format(name)
        if os.path.isfile(fname):
            os.remove(fname)

    fname = 'datapackage.json'
    if os.path.isfile(fname):
        os.remove(fname)
# *******************************************************************

# *******************************************************************
#  Read utilities
#  Returns a dataframe depending on the case: confirmed, deaths, recovered
# *******************************************************************
def read_data(case):
    fname = 'time_series_19-covid-{}.csv'.format(case)
    df = read_csv(fname)
    return df

def read_confirmed_cases():
    return read_data('Confirmed')

def read_recovered_cases():
    return read_data('Recovered')

def read_deaths_cases():
    return read_data('Deaths')
# *******************************************************************


# =================================================================
def normalize_date(date):
    month, day, year = date.split('/')
    return '{day}/{month}'.format(day=day, month=month)


# =================================================================
def select_data_by_country(df, country):
    key_selection = 'Country/Region'
    # TODO improve the case such as France
    if country == 'France':
        key_selection = 'Province/State'

    dc = df[df[key_selection] == country]
    to_remove = ('Province/State', 'Country/Region', 'Lat', 'Long')
    for a in to_remove:
        dc.pop(a)

    t, y = zip(*list(dc.items()))

    # new format
    y = np.array([int(_) for _ in y])
    t = list(map(normalize_date, t))

    return t,y


# =================================================================
def plot_matplotlib(df):
    """
    used for testing
    """
    from matplotlib import pyplot as plt

    fig, ax = plt.subplots()

    countries = ['Morocco', 'Tunisia', 'Italy', 'Spain', 'France', 'Germany']

    for country in countries:
        t,y = select_data_by_country(df, country)

    #    ax.plot(t, y, '-', label=country)
        ax.semilogy(t, y, '-', label=country)
        ax.set_xticks(t[::7]+[t[-1]])
        ax.set_xlabel('Date',size=12,fontweight='semibold')
        ax.set_ylabel('Confirmed cases',size=12,fontweight='semibold')

    plt.legend()
    plt.show()

# =================================================================
def load_country_map(country):
    """ contours for a country """

    # ...
    fname = '../datasets/{country}/contours.yml'.format(country=country.lower())
    with open(fname) as f:
        d = yaml.load(f, Loader=yaml.Loader)
        d_contours = {}
        for k,v in d.items():
            x = np.array(v, dtype=int)
            y = x.reshape((len(x)//2,2))
            d_contours[k] = y
    # ...

    return d_contours

# =================================================================
def plotly_country_map(province, contour, highlighted=False):

    x = contour[:,0]
    y = contour[:,1]

    fillcolor = '#777495'
    if highlighted:
        fillcolor = '#C9B7BA'

    line_marker = dict(color='#455462', width=2)

    trace_crv = go.Scatter(
        x=x,
        y=y,
        mode = 'lines',
        name=province,
        line=line_marker,
        fill='toself',
        fillcolor = fillcolor,
    )

    return [trace_crv]

# =================================================================
def plotly_country_n_patients(d_barycenters, df):
    # ...
    n_patients = []
    x = []
    y = []
    for province, barycenter in d_barycenters.items():
        x.append(barycenter[0])
        y.append(barycenter[1])

        _df = df[df['province'] == province]
        n = len(_df.index)
        n_patients.append(n)
    # ...
    
    df_RD = getDfRecoveredDeathsHospitalized(n_patients)
    
    trace = go.Scatter(
        x=x,
        y=y,
        mode = 'markers',
        marker=dict(color='red'),
        marker_size=[(i/6) for i in n_patients],
        textposition='bottom center',
        hovertext=['Hospitalized: '+ str(row['hospitalized']) + ' | Recovered: ' + str(row['recovered']) + ' | Deaths: ' + str(row['deceased']) + ' | Total: '+ str(row['cases']) + " cases" for index,row in df_RD.iterrows()],
        hoverinfo='text'
    )
    return { 'trace':[trace], 'df_RD': df_RD}

# =================================================================
def load_country_patients(country):
    # TODO take patients.csv
    fname = '../datasets/{country}/patients-test.csv'.format(country=country.lower())
    df = read_csv(fname)
    return df

# =================================================================
def load_country_statistics_age(country):
    fname = '../datasets/{country}/statistiques-age.csv'.format(country=country.lower())
    df = read_csv(fname)
    return df

# =================================================================
def load_country_statistics_gender(country):
    fname = '../datasets/{country}/statistiques-sex.csv'.format(country=country.lower())
    df = read_csv(fname)
    return df

# =================================================================
def load_country_statistics_global_recovered_deceased(country):
    fname = '../datasets/{country}/statistiques-global-recovered-deceased.csv'.format(country=country.lower())
    df = read_csv(fname)
    return df

# =================================================================
def load_country_statistics_recovered_deceased(country):
    # TODO take patients.csv
    fname = '../datasets/{country}/statistiques-recovered-deceased.csv'.format(country=country.lower())
    df = read_csv(fname)
    return df

def getDfRecoveredDeathsHospitalized(n_patients):
    df_RD = load_country_statistics_recovered_deceased('morocco')
    df_RD['cases'] = n_patients
    df_RD['hospitalized'] = df_RD['cases'] - (df_RD['recovered'] + df_RD['deceased'])
    return df_RD
# =================================================================
def compute_barycenters(d_contours):
    d_barycenters = {}
    for province, contour in d_contours.items():
        d_barycenters[province] = (contour[:,0].mean(), contour[:,1].mean())

    return d_barycenters

# =================================================================
def select_by_date(df, date_key, start_date, end_date):

    if start_date is not None:
        start_date = dt.strptime(start_date.split('T')[0], '%Y-%m-%d')

    if end_date is not None:
        end_date = dt.strptime(end_date.split('T')[0], '%Y-%m-%d')

    df[date_key] = pd.to_datetime(df[date_key])

    mask = True
    if start_date is not None:
        mask = mask & (df[date_key] >= start_date)

    if end_date is not None:
        mask = mask & (df[date_key] <= end_date)

    df = df.loc[mask]
    return df



########################################################################
if __name__ == '__main__':
#    clean_dataset()
#    update_dataset()

    df = read_confirmed_cases()
    plot_matplotlib(df)
