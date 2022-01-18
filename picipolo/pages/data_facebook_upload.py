import streamlit as st
import pandas as pd


def app():
    st.markdown("## Data FB Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file `friend_requests_received.csv`.")
    st.write("\n")

    # Code to read a single file
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'], key=1)
    global data1
    if uploaded_file is not None:
        try:
            data1 = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data1 = pd.read_excel(uploaded_file)

    if st.button("Load Data", key=1):
        # Raw data
        st.dataframe(data1)
        data1.to_csv('data/friend_requests_received.csv', index=False)

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file `friend_requests_sent.csv`.")
    st.write("\n")

    # Code to read a single file
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'], key=2)
    global data2
    if uploaded_file is not None:
        try:
            data2 = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data2 = pd.read_excel(uploaded_file)

    if st.button("Load Data", key=2):
        # Raw data
        st.dataframe(data2)
        data2.to_csv('data/friend_requests_sent.csv', index=False)

    st.markdown("### Upload a csv file `friend_requests_rejected.csv`.")
    st.write("\n")

    # Code to read a single file
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'], key=3)
    global data3
    if uploaded_file is not None:
        try:
            data3 = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data3 = pd.read_excel(uploaded_file)


    if st.button("Load Data", key=3):
        # Raw data
        st.dataframe(data3)
        data3.to_csv('data/friend_requests_rejected.csv', index=False)

    st.markdown("### Upload a csv file `friends.csv`.")
    st.write("\n")

    # Code to read a single file
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'], key=4)
    global data4
    if uploaded_file is not None:
        try:
            data4 = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data4 = pd.read_excel(uploaded_file)

    if st.button("Load Data", key=4):
        # Raw data
        st.dataframe(data4)
        data4.to_csv('data/friends.csv', index=False)
