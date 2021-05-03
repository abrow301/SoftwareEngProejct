import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')

app = dash.Dash()

# Bar chart data
barchart_df = df1
barchart_df = barchart_df.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['NOC'], y=barchart_df['Total'])]

# Stack bar chart data
stackbarchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
stackbarchart_df = stackbarchart_df.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()
trace1_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Bronze'], name='Bronze',
                              marker={'color': '#CD7F32'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Silver'], name='Silver',
                              marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Gold'], name='Gold',
                              marker={'color': '#FFD700'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]


# Line Chart
line_df = df1
line_df['date'] = pd.to_datetime(line_df['date'])
data_linechart = [go.Scatter(x=line_df['date'], y=line_df['actual_max_temp'], mode='lines', name='Temperature')]

# Multi Line Chart
multiline_df = df1
multiline_df['date'] = pd.to_datetime(multiline_df['date'])
trace1_multiline = go.Scatter(x=multiline_df['date'], y=multiline_df['actual_min_temp'], mode='lines', name='Min Temp')
trace2_multiline = go.Scatter(x=multiline_df['date'], y=multiline_df['actual_max_temp'], mode='lines', name='Max Temp')
trace3_multiline = go.Scatter(x=multiline_df['date'], y=multiline_df['actual_mean_temp'], mode='lines', name='Mean Temp')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble chart
bubble_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

data_bubblechart = [
    go.Scatter(x=bubble_df['average_min_temp'],
               y=bubble_df['average_max_temp'],
               text=bubble_df['date'],
               mode='markers',
               marker=dict(size=bubble_df['average_max_temp'] / 200, color=bubble_df['average_max_temp'] / 200, showscale=True))
]

# Heatmap
data_heatmap = [go.Heatmap(x=df1['day'],
                           y=df1['month'],
                           z=df1['record_max_temp'].values.tolist(),
                           colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Total Number of Medals for each Country at the 2016 Rio Olympic Games', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of medals won from the country of selected continent.'),
    dcc.Graph(id='graph1'),
    html.Div('Please select a continent', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-continent',
        options=[
            {'label': 'Asia', 'value': 'Asia'},
            {'label': 'Africa', 'value': 'Africa'},
            {'label': 'Europe', 'value': 'Europe'},
            {'label': 'North America', 'value': 'North America'},
            {'label': 'Oceania', 'value': 'Oceania'},
            {'label': 'South America', 'value': 'South America'}
        ],
        value='Europe'
    ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of total Olympic Medals by Country in the 2016 Rio Olympics.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Number of total Olympic Medals by Country in the 2016 Rio Olympics',
                                      xaxis={'title': 'States'}, yaxis={'title': 'Number of total Olympic Medals'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represents the Olympic Medals by grade by Countries in the 2016 Rio Olympic Games.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Olympic Medals by grade by Countries in the 2016 Rio Olympic Games',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Number of Olympic Medals'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the Max Temperatures for the months of the years 2014-2015.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Max Temperatures for the months of the years 2014-2015',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the Min, Max, and Mean Temperatures for the months of the years 2014-2015.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Min, Max, and Mean Temperatures for the months of the years 2014-2015',
                      xaxis={'title': 'Date'}, yaxis={'title': 'Temperatures'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represent the Mean Temperatures for the months of the years 2014-2015.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Mean Temperatures for the months of the years 2014-2015',
                                      xaxis={'title': 'Months'}, yaxis={'title': 'Temperatures'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the Recorded Max temps of the years 2014-2015.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Recorded Max temps of the years 2014-2015',
                                      xaxis={'title': 'Day of Week'}, yaxis={'title': 'Month of Year'})
              }
              )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_continent):

    new_df = filtered_df.groupby(['NOC'])['Total'].sum().reset_index()
    new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Total Number of Medals in the 2016 Rio Olympic Games by Country  '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of Total Medals'})}


if __name__ == '__main__':
    app.run_server()
