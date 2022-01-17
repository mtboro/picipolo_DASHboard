import streamlit as st
from pages.plots import utils

def app():
    df = utils.load_data()
    df = df.groupby('name')['text'].count()   
    st.write(df)
    