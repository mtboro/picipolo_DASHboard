import streamlit as st
from datetime import datetime
from pages.plots import heatmap


def app():
    st.markdown("## Data Upload")

    data = heatmap.load_data()

    start = data['time'].min()
    end = datetime.now()

    name = st.text_input('Please provide your name', 'John Doe')

    fig = heatmap.create_heatmap(data, start, end, me=name)

    st.plotly_chart(fig, use_container_width=True)


