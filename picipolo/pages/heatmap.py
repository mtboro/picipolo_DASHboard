import streamlit as st
from datetime import datetime
from pages.plots import heatmap, utils, line_chart_messages


def app():
    st.markdown("## Heatmap")

    data = utils.load_data()

    start = data['time'].min()
    end = datetime.now()

    name = st.text_input('Please provide your name', 'John Doe')

    fig = heatmap.create_heatmap(data, start, end, me=name)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## Line chart")
    line_chart = line_chart_messages.create_plot()
    st.plotly_chart(line_chart, use_container_width=True)
    st.plotly_chart()
