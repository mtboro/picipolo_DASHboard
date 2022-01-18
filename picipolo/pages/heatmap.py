import streamlit as st
from datetime import datetime
from pages.plots import heatmap, utils, line_chart_messages


def app():
    st.markdown("## Heatmap")

    data = utils.load_data()

    if data is None:
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        default_start = data['time'].min().date()
        default_end = datetime.now().date()
        
        name = st.text_input('Please provide your name', 'John Doe', key="name")

        col1, col2 = st.columns(2)

        with col1:
            start = st.date_input('Start', default_start)
        with col2:
            end = st.date_input('End', default_end)

        fig = heatmap.create_heatmap(data, start, end, me=name)

        st.plotly_chart(fig, use_container_width=True)

        name2 = st.text_input('Please provide your name', 'John Doe', key="name2")

        if name2 != "John Doe":
            st.markdown("## Line chart")
            line_chart = line_chart_messages.create_plot(name2)
            st.plotly_chart(line_chart, use_container_width=True)
        else:
            st.markdown("Please fill `name field` to get analysis")

