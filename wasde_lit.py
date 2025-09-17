import streamlit as st
import os
import pandas as pd
import plotly.express as px

world = pd.read_csv('world.csv')

st.subheader('World Cotton Supply and Use Historical Revisions')
st.caption('Choose a crop year, then click Run')

def cy(crop_year, attribute):
    fig1 = px.bar(world[(world.MarketYear == crop_year) & (world.Attribute == attribute)].pivot(index='ReleaseDate', columns='Region', values='Value').sort_index().astype(float).diff().drop(columns=['Major Exporters','Major Importers','Total Foreign','World Less China','S. Hemis.']), barmode='group', color_continuous_scale=px.colors.sequential.Oranges, text='Region',title=f'{crop_year} {attribute}', labels={attribute})
    return st.plotly_chart(fig1)


def execute():
    if cy2024: cy('2024/25','Production'), cy('2024/25','Imports'), cy('2024/25', 'Domestic Use'), cy('2024/25','Exports'), cy('2024/25', 'Ending Stocks')
    if cy2025: cy('2025/26','Beginning Stocks'), cy('2025/26','Production'), cy('2025/26', 'Imports'), cy('2025/26', 'Domestic Use'), cy('2025/26', 'Exports'), cy('2025/26', 'Ending Stocks')





# Sidebar configurations
cy2024 = st.sidebar.checkbox('2024/25', key='a')
cy2025 = st.sidebar.checkbox('2025/26', key='b')




run_btn = st.sidebar.button('Run', on_click=execute, key='z')
