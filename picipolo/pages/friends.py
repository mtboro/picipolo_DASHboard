import os
import streamlit as st
from pages.plots import bar_chart


def app():
    if 'friends.csv' not in os.listdir('data/user_data') or \
            'friend_requests_received.csv' not in os.listdir('data/user_data') or \
            'friend_requests_sent.csv' not in os.listdir('data/user_data') or \
            'friend_requests_rejected.csv' not in os.listdir('data/user_data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        config = {'displayModeBar': False, 'scrollZoom': False}
        st.markdown("## Friends analysis")
        fig1, fig2, fig3, fig4 = bar_chart.create_chart()
        st.plotly_chart(fig1, config=config, use_container_width=True)
        st.plotly_chart(fig2, config=config, use_container_width=True)
        st.plotly_chart(fig3, config=config, use_container_width=True)
        st.plotly_chart(fig4, config=config, use_container_width=True)
