import streamlit as st
import pandas as pd
from pathlib import Path


def app():
    st.markdown("## Data Upload")

    st.markdown("### Upload a csv file for analysis.")
    st.write("\n")

    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

    global data
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file, delimiter=';')
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)

    if st.button("Load Data"):
        # Display raw data
        st.dataframe(data.head())

        file_path = Path(__file__).resolve()
        data_path = file_path.parents[2].joinpath('data', 'user_data', 'parsed', 'messengerData.csv')
        data.to_csv(data_path, index=False, sep=';')
