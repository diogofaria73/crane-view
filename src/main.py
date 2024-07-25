import ssl
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

from datetime import datetime
from repository.data_repository import load_crane_infos
from repository.indicators_services import calculate_payments
from pages.cranes import cranes
from pages.outcomes import outcomes

# Setup SSL certificate to run requests
ssl._create_default_https_context = ssl._create_unverified_context
# Page Layout
st.set_page_config(page_title='Equipment Tracking - Radix Mockup',  layout="wide",
                   page_icon='../assets/skyscraper-with-antennas.png',
                   initial_sidebar_state="collapsed"
                   )

df_cranes_info = load_crane_infos()

cranes(df_cranes_info)
