import streamlit as st
import pandas as pd


def load_crane_infos():
    df = pd.read_json('dataset/cranes.json')
    return df
