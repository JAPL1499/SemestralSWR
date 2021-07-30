# Integrantes: Alpírez, Margie -- Brito, Bryan -- Domínguez, Jorge -- Paredes, José
# correos: margie.alpirez@utp.ac.pa -- bryan.brito@utp.ac.pa -- jorge.dominguez3@utp.ac.pa -- jos.paredes@utp.ac.pa

import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)
server = app.server

# ---------------------------------------------------------------

# Taken from https://data.townofcary.org/explore/dataset/solid-waste-and-recycling-collection-routes/table/?disjunctive.day
data = pd.read_csv('solid-waste-and-recycling-collection-routes.csv', error_bad_lines=False, sep=";")

# ---------------------------------------------------------------
# COLLECTION DAY
day_count = data['day'].value_counts(ascending=True).reset_index()
day_count.columns = ['Days', 'Count']
cd_fig = px.line(day_count, x='Days', y='Count', title="COLLECTION DAYS")

# ---------------------------------------------------------------
# RECYCLE WEEK
rw_df_1 = data[['day', 'cycle']].copy()
rw_df_2 = rw_df_1.groupby(['day', 'cycle']).size().reset_index()
rw_df_2.columns = ['Days', 'Recycle Week', 'Count']
rw_fig = px.bar(rw_df_2, x='Recycle Week', y='Count', color='Days', title="RECYCLE WEEK", barmode='group')

# ---------------------------------------------------------------
# SOLID WASTE PICKUP
sw_df_1 = data[['day', 'sw_pickup']].copy()
sw_df_2 = sw_df_1.groupby(['day', 'sw_pickup']).size().reset_index()
sw_df_2.columns = ['Days', 'Solid Waste Pickup', 'Count']
sw_fig = px.bar(sw_df_2, x='Days', y='Count', color='Solid Waste Pickup', title="SOLID WASTE PICKUP")

# ---------------------------------------------------------------
# RECYCLING PICKUP
rec_df_1 = data[['day', 'rec_pickup']].copy()
rec_df_2 = rec_df_1.groupby(['day', 'rec_pickup']).size().reset_index()
rec_df_2.columns = ['Days', 'Recycling Pickup', 'Count']
rec_fig = px.bar(rec_df_2, x='Days', y='Count', color='Recycling Pickup', title="RECYCLING PICKUP", barmode='group')

# ---------------------------------------------------------------
# YARD WASTE PICKUP
yw_df_1 = data[['day', 'yw_pickup']].copy()
yw_df_2 = yw_df_1.groupby(['day', 'yw_pickup']).size().reset_index()
yw_df_2.columns = ['Days', 'Yard Waste Pickup', 'Count']
yw_fig = px.bar(yw_df_2, x='Days', y='Count', color='Yard Waste Pickup', title="YARD WASTE PICKUP")


# ---------------------------------------------------------------
# LAYOUT
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
    ),

    dcc.Graph(
        id='solid-waste-pickup',
        figure=sw_fig
    ),

    dcc.Graph(
        id='recycling-pickup',
        figure=rec_fig
    ),

    dcc.Graph(
        id='yard-waste-pickup',
        figure=yw_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
