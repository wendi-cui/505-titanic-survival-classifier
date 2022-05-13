import dash
from dash import dcc, html
import pandas as pd

filepath='resources/final_probs.csv'
df=pd.read_csv(filepath)
names=df['Name'].values
index=df['Name'].index.values
nameslist = list(zip(index, names))
fare_list = ['Fare (0, 10]','Fare (10, 20]', 'Fare (20, 30]', 'Fare (30, 40]', 'Fare (40, 50]',
       'Fare (50, 60]', 'Fare (60, 70]', 'Fare (70, 80]', 'Fare (80, 90]',
       'Fare (90, 100]', 'Fare (100, 110]', 'Fare (110, 120]',
       'Fare (120, 140]', 'Fare (140, 150]', 'Fare (150, 160]',
       'Fare (160, 170]', 'Fare (170, 220]', 'Fare (220, 240]',
       'Fare (240, 250]', 'Fare (250, 270]', 'Fare (270, 600]']

tab_4_layout = html.Div([
    html.H3('Would you survive the Titanic?'),
    html.Div([
        html.Div('Select:', className='one column'),
        # Title,
        html.Div([
            html.Div('Siblings and Spouses'),
            dcc.Dropdown(
                id='family_dropdown',
                options=[{'label': i, 'value': i} for i in range(0,9)],
                value='2',
                ),
        ],className='two columns'),
        html.Div([
            html.Div('Age'),
            dcc.Dropdown(
                id='age_dropdown',
                options=[{'label': i, 'value': i} for i in range(1,81)],
                value='25',

                ),
        ],className='two columns'),
        html.Div([
            html.Div('Fare'),
            dcc.Dropdown(
                id='fare_dropdown',
                options=[{'label': fare_list[i], 'value': i} for i in range(len(fare_list))],
                value='1',

                ),
        ],className='two columns'),
        html.Div([
            html.Div('Cabin Class'),
            dcc.Dropdown(
                id='cabin_dropdown',
                options=[{'label': i, 'value': i} for i in ['First', 'Second', 'Third']],
                value='First',
                ),
        ],className='two columns'),
        html.Div('     ', className='one column')
    ],className='twelve columns'),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div('Select:', className='one column'),
        html.Div([
            html.Div('Title'),
            dcc.RadioItems(
                id='title_radio',
                options=[{'label': i, 'value': i} for i in ['Mr.', 'Miss', 'Mrs.', 'VIP']],
                value='None',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Sex'),
            dcc.RadioItems(
                id='sex_radio',
                options=[{'label': i, 'value': i} for i in ['Male', 'Female']],
                value='None',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Port of Embarkation'),
            dcc.RadioItems(
                id='port_radio',
                options=[{'label': i, 'value': i} for i in ['Cherbourg', 'Queenstown', 'Southampton']],
                value='None',
                ),
        ],className='five columns'),
    ],className='twelve columns'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    # Output results
    html.Div([
        html.Div(id='user-inputs-box', style={'text-align':'center','fontSize':18}),
        html.Div(id='final_prediction', style={'color':'red','text-align':'center','fontSize':18})
    ],className='twelve columns'),



])
