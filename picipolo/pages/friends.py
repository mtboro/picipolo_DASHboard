import os
import streamlit as st
from plots import heatmap_friends


def app():
    if 'friends.csv' not in os.listdir('data/user_data') or \
            'friend_requests_received.csv' not in os.listdir('data/user_data') or \
            'friend_requests_sent.csv' not in os.listdir('data/user_data') or \
            'friend_requests_rejected.csv' not in os.listdir('data/user_data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        config = {'displayModeBar': False}
        st.markdown("## Friends analysis")

        st.plotly_chart(heatmap_friends.create_chart(), config=config, use_container_width=True)
