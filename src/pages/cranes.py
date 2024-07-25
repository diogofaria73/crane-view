import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
from services.chart_builder import chartBuilder


def cranes(df: pd.DataFrame):

    with st.container():

        st.title('Cranes List')

        selected_status = st.multiselect(
            'Selecione o estado de localização do equipamento', df['state'].unique(), placeholder="Região do Brasil")

        st.divider()

        if selected_status != []:
            df_filtered = df[df['Status'].isin(
                selected_status)]

            st.dataframe(df_filtered, use_container_width=True,
                         selection_mode='multiple')

        else:
            st.dataframe(df, use_container_width=True)

        st.divider()

        col2, col3 = st.columns(2)

        col2.plotly_chart(chartBuilder('bar', df),
                          use_container_width=True)

        col3.plotly_chart(chartBuilder('pie', df),
                          use_container_width=True)
