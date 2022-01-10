import streamlit as st

from multipage import MultiPage
from pages import data_upload, heatmap

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

app.add_page("Upload Data", data_upload.app)
app.add_page("Heatmap", heatmap.app)

if __name__ == '__main__':
    app.run()
