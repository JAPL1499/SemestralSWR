import pandas as pd
import plotly.express as px
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

#---------------------------------------------------------------
#Taken from https://data.townofcary.org/explore/dataset/solid-waste-and-recycling-collection-routes/table/?disjunctive.day
data = pd.read_csv("solid-waste-and-recycling-collection-routes.csv",error_bad_lines=False,sep=";")

#---------------------------------------------------------------
#COLLECTION DAY
day_count = data["day"].value_counts(ascending=True).reset_index()
day_count.columns = ['Days', 'Counts']
cd_fig = px.line(day_count,x='Days', y='Counts',title="COLLECTION DAYS")

#---------------------------------------------------------------
#RECYCLE WEEK
rw_df_1 = data[['day', 'cycle']].copy()
rw_df_2 = rw_df_1.groupby(['day','cycle']).size().reset_index()
rw_df_2.columns = ['Days', 'Recycle Week', 'Count']
rw_fig = px.bar(rw_df_2, x ='Recycle Week', y = "Count", color='Days',title="RECYCLE WEEK",barmode='group' )

#---------------------------------------------------------------
#COLLECTION DAY

#---------------------------------------------------------------
#COLLECTION DAY

#---------------------------------------------------------------
#COLLECTION DAY
#---------------------------------------------------------------
#LAYOUT
app.layout = html.Div(children=[
    html.H1(children='Solid Waste and Recycling Collection'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='collection-day',
        figure=cd_fig
    ),

    dcc.Graph(
        id='recycle-week',
        figure=rw_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
