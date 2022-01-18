import streamlit as st
import pandas as pd
from pages.plots import utils


def app():
    df = utils.load_data()
    if df is None:
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        df = df.groupby('name')['text'].count()
        df = pd.DataFrame(df)
        df = df.sort_values(by='text', ascending=False)
        df.columns = ['count']
        st.write(df.head(20))
