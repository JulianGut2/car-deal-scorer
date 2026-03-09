import streamlit as st
import pandas as pd
from src.data_cleaner import clean_data
import joblib

model = joblib.load("data/model.pkl")

st.set_page_config(page_title = 'Car Deal Scorer', layout = "wide")

df = clean_data(pd.read_csv("data/vehicles.csv"))

with st.sidebar:
    year = st.selectbox("Year", sorted(df["year"].dropna().astype(int).unique()))

