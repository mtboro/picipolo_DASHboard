import streamlit as st

from multipage import MultiPage
from pages import data_upload, heatmap, wordcloudpage, data_facebook_upload, friends, messageranking

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Facebook analysis")

app.add_page("Upload Messenger Data", data_upload.app)
app.add_page("Upload FB Data", data_facebook_upload.app)
app.add_page("Messages", heatmap.app)
app.add_page("Friends", friends.app)
app.add_page("Wordcloud", wordcloudpage.app)
app.add_page("Ranking", messageranking.app)

if __name__ == '__main__':
    app.run()
