import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sklearn import preprocessing




# Load CSV file from Datasets folder
dfBitcoin = pd.read_csv('../Datasets/coin_Bitcoin.csv')
dfEthereum = pd.read_csv('../Datasets/coin_Ethereum.csv')
dfCloses = pd.read_csv('../Datasets/coin_Closes.csv')

app = dash.Dash()

# Bar chart data
barchart_df = dfBitcoin
barchart_df = barchart_df.sort_values(by=['Close'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['Date'], y=barchart_df['Close'])]

# Stack bar chart data
stackbarchart_df = dfEthereum.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
stackbarchart_df = stackbarchart_df.sort_values(by=['Close'], ascending=[False]).head(20).reset_index()
trace1_stackbarchart = go.Bar(x=stackbarchart_df['Date'], y=stackbarchart_df['Low'], name='Low Price',
                              marker={'color': '#CD7F32'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['Date'], y=stackbarchart_df['High'], name='High Price',
                              marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['Date'], y=stackbarchart_df['Close'], name='Close Price',
                              marker={'color': '#FFD700'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]


# Line Chart
line_df = dfEthereum
line_df['Date'] = pd.to_datetime(line_df['Date'])
data_linechart = [go.Scatter(x=line_df['Date'], y=line_df['Close'], mode='lines', name='Close Prices')]

# Multi Line Chart
multiline_df = dfEthereum
multiline_df['Date'] = pd.to_datetime(multiline_df['Date'])
trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Low'], mode='lines', name='Low Price')
trace2_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['High'], mode='lines', name='High Price')
trace3_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Close'], mode='lines', name='Close Price')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Heatmap
data_heatmap = [go.Heatmap(x=dfEthereum['Date'],
                           y=dfEthereum['Volume'],
                           z=dfEthereum['Close'].values.tolist(),
                           colorscale='Jet')]

#Scaled Line graph on a 1 to 0 scale
#Eth = pd.read_csv('../Datasets/coin_Ethereum.csv', index_col=['Date'])
#Bit = pd.read_csv('../Datasets/coin_Bitcoin.csv', index_col=['Date'])
#main_data = pd.DataFrame({'Ethereum' : Eth['Close'],
                          #'Bitcoin' : Bit['Close']})
#min_max_scaler = preprocessing.MinMaxScaler()
#norm_data = pd.DataFrame(min_max_scaler.fit_transform(main_data), columns=main_data.columns, index=main_data.index)
#norm_data['Date'] = pd.to_datetime(norm_data['Date'])
#trace1_scaledline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Ethereum'], mode='lines', name='Ethereum')
#trace2_scaledline = go.Scatter(x=multiline_df['Date'], y=multiline_df['BitCoin'], mode='lines', name='Bitcoin')
#data_scaledline = [trace1_scaledline, trace2_scaledline]



# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Close values for different types of crypto currencies', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Line Graph', style={'color': '#df1e56'}),
    html.Div('This line graph represent the price of each currency when the market closed for that day.'),
    dcc.Graph(id='graph1'),
    html.Div('Please select a Currency', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-currency',
        options=[
            {'label': 'Bitcoin', 'value': 'Bitcoin'},
            {'label': 'Ethereum', 'value': 'Ethereum'},
        ],
        value='Bitcoin'
    ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This Bar chart represent the price of Bitcoin at close value'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Price of Bitcoin at close value',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Close Prices'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represents the Low, High, and Close Prices of Bitcoin.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='The Low, High, and Close Prices of Bitcoin',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Values'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the change in the closing value of Ethereum.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Change in the closing value of Ethereum',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Closing Value'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the Low, High, and Closing prices for Ethereum.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Low, High, and Closing prices for Ethereum',
                      xaxis={'title': 'Date'}, yaxis={'title': 'Values'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represents the Closing values based on the date and volume of Ethereum.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Closing values based on the date and volume of Ethereum',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Volume'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Scaled Multi Line chart', style={'color': '#df1e56'}),
        html.Div(
            'This scaled line chart represent the Closing prices of Bitcoin and Ethereum on a 0 to 1 scale.'),
        dcc.Graph(id='graph7',
                  figure={
                      'data': data_multiline,
                      'layout': go.Layout(
                          title='Closing prices of Bitcoin and Ethereum on a 0 to 1 scale',
                          xaxis={'title': 'Date'}, yaxis={'title': 'Values'})
                  }
                  )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-currency', 'value')])
def update_figure(selected_currency):
    filtered_df = dfCloses[dfCloses['Name'] == selected_currency]

    new_df = filtered_df.groupby(['Date'])['Close'].sum().reset_index()
    new_df['Date'] = pd.to_datetime(new_df['Date'])
    data_interactive_linegraph = [go.Scatter(x=new_df['Date'], y=new_df['Close'], mode='lines', name='Close Prices')]
    return {'data': data_interactive_linegraph, 'layout': go.Layout(title='Close values for different types of crypto currencies   '+selected_currency,
                                                                   xaxis={'title': 'Date'},
                                                                   yaxis={'title': 'Close Values'})}


if __name__ == '__main__':
    app.run_server()
