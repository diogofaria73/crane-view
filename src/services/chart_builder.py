import pandas as pd
import plotly.express as px
import streamlit as st


def chartBuilder(chart_type, data: pd.DataFrame):

    if chart_type == 'bar':
        chart_render = px.bar(data, x='equipment_model',
                              y='price',
                              title='Precificação por Modelo de Equipamento',
                              color='equipment_model',
                              color_continuous_scale=px.colors.sequential.Blues)

        return chart_render

    elif chart_type == 'pie':
        chart_render = px.pie(
            data, values=data.groupby(
                'state')['equipment_status'].count().values,
            names=data['state'].unique(),
            title='Distribuição de Equipamentos por Estados do Pais',
            labels={'value': 'Quantidade', 'names': 'Estado'}, color_discrete_map=px.colors.qualitative.Prism)

        return chart_render
