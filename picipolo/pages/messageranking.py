import streamlit as st
import pandas as pd
from pages.plots import utils

def app():
    df = utils.load_data()
    df = df.groupby('name')['text'].count()
    df = pd.DataFrame(df)
    df = df.sort_values(by='text', ascending=False)
    df.columns = ['count']
    st.write(df.head(20))
    
