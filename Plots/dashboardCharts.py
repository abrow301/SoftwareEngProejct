import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from sklearn import preprocessing

# Load CSV file from Datasets folder

dfAave = pd.read_csv('../Datasets/coin_Aave.csv')
dfBinanceCoin = pd.read_csv('../Datasets/coin_BinanceCoin.csv')
dfBitcoin = pd.read_csv('../Datasets/coin_Bitcoin.csv')
dfCardano = pd.read_csv('../Datasets/coin_Cardano.csv')
dfChainLink = pd.read_csv('../Datasets/coin_ChainLink.csv')
dfCosmos = pd.read_csv('../Datasets/coin_Cosmos.csv')
dfCryptocomCoin = pd.read_csv('../Datasets/coin_CryptocomCoin.csv')
dfDogeCoin = pd.read_csv('../Datasets/coin_DogeCoin.csv')
dfEOS = pd.read_csv('../Datasets/coin_EOS.csv')
dfEthereum = pd.read_csv('../Datasets/coin_Ethereum.csv')
dfIota = pd.read_csv('../Datasets/coin_Iota.csv')
dfLiteCoin = pd.read_csv('../Datasets/coin_LiteCoin.csv')
dfMonero = pd.read_csv('../Datasets/coin_Monero.csv')
dfNEM = pd.read_csv('../Datasets/coin_NEM.csv')
dfPolkadot = pd.read_csv('../Datasets/coin_Polkadot.csv')
dfSolana = pd.read_csv('../Datasets/coin_Solana.csv')
dfStellar = pd.read_csv('../Datasets/coin_Stellar.csv')
dfTether = pd.read_csv('../Datasets/coin_Tether.csv')
dfTron = pd.read_csv('../Datasets/coin_Tron.csv')
dfUniswap = pd.read_csv('../Datasets/coin_Uniswap.csv')
dfUSDCoin = pd.read_csv('../Datasets/coin_USDCoin.csv')
dfWrappedBitCoin = pd.read_csv('../Datasets/coin_WrappedBitCoin.csv')
dfXRP = pd.read_csv('../Datasets/coin_XRP.csv')
dfAll = pd.read_csv('../Datasets/coin_All_Close.csv')

app = dash.Dash()

# Line Chart
line_df = dfBitcoin
line_df['Date'] = pd.to_datetime(line_df['Date'])
data_linechart = [go.Scatter(x=line_df['Date'], y=line_df['Close'], mode='lines', name='Temperature')]

# Multi Line Chart
multiline_df = dfBitcoin
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

#Scaled Multi Line Chart
Eth = dfEthereum
Eth['Date'] = pd.to_datetime(Eth['Date'])
Bit = dfBitcoin
Bit['Date'] = pd.to_datetime(Bit['Date'])
Doge = dfDogeCoin
Doge['Date'] = pd.to_datetime(Doge['Date'])
main_data = pd.DataFrame({'Ethereum' : Eth['Close'],
                          'Bitcoin' : Bit['Close'],
                          'Dogecoin' : Doge['Close'] })
min_max_scaler = preprocessing.MinMaxScaler()
norm_data = pd.DataFrame(min_max_scaler.fit_transform(main_data))



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
    html.H3('Interactive Line graph', style={'color': '#df1e56'}),
    html.Div('This line graph represent the price of each currency when the market closed for that day.'),
    dcc.Graph(id='graph1'),
    html.Div('Please select a currency', style={'color': '#ef3e18', 'margin':'10px'}),
    html.Hr(style={'color': '#7FDBFF'}),

    dcc.Dropdown(
        id='select-currency',
        options=[
            {'label': 'Aave', 'value': 'Aave'},
            {'label': 'BinanceCoin', 'value': 'BinanceCoin'},
            {'label': 'Bitcoin', 'value': 'Bitcoin'},
            {'label': 'Cardano', 'value': 'Cardano'},
            {'label': 'ChainLink', 'value': 'ChainLink'},
            {'label': 'Cosmos', 'value': 'Cosmos'},
            {'label': 'CryptocomCoin', 'value': 'CryptocomCoin'},
            {'label': 'Dogecoin', 'value': 'Dogecoin'},
            {'label': 'EOS', 'value': 'EOS'},
            {'label': 'Ethereum', 'value': 'Ethereum'},
            {'label': 'Iota', 'value': 'Iota'},
            {'label': 'Litecoin', 'value': 'Litecoin'},
            {'label': 'Monero', 'value': 'Monero'},
            {'label': 'NEM', 'value': 'NEM'},
            {'label': 'Polkadot', 'value': 'Polkadot'},
            {'label': 'Solana', 'value': 'Solana'},
            {'label': 'Stellar', 'value': 'Stellar'},
            {'label': 'Tether', 'value': 'Tether'},
            {'label': 'Tron', 'value': 'Tron'},
            {'label': 'Uniswap', 'value': 'Uniswap'},
            {'label': 'USDCoin', 'value': 'USDCoin'},
            {'label': 'WrappedBitcoin', 'value': 'WrappedBitcoin'},
            {'label': 'XRP', 'value': 'XRP'}

        ],
        value='Bitcoin'
    ),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the price of Bitcoin at close value'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Close value of Bitcoin',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Close Value'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the Low, High, and Close prices of Bitcoin.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Low, High, and Close prices of Bitcoin',
                      xaxis={'title': 'Date'}, yaxis={'title': 'Prices'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the Close value of Ethereum based on the volume of the currency.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Close value of Ethereum based on the volume of the currency',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Volume'})
              }
              ),

    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This Scaled Line graph is to compare the Close prices of different Crypto Currencies base don a 0 to 1 scale.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': norm_data,
                  'layout': go.Layout(title='Scaled Close prices of Bitcoin, Ethereum, and Dogecoin',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Close Price'})
              }
              )


])



@app.callback(Output('graph1', 'figure'),
              [Input('selected_currency', 'value')])
def update_figure(selected_currency):
    filtered_df = dfAll[dfAll['Name'] == selected_currency]

    new_df = filtered_df.groupby(['Name'])['Close'].sum().reset_index()
    new_df = new_df.sort_values(by=['Name'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Scatter(x=new_df['Date'], y=new_df['Close'], mode='lines', name='Prices')]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Closing prices for different types of crypto currency  '+selected_currency,
                                                                   xaxis={'title': 'Currency'},
                                                                   yaxis={'title': 'Close Prices over time'})}


if __name__ == '__main__':
    app.run_server()