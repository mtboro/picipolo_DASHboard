import streamlit as st
import matplotlib.pyplot as plt
import random
from pages.plots import generate_wordcloud, generate_emoji_wordcloud, utils


def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")
    return plt


def app():
    df = utils.load_data()

    if df is None:
        st.markdown("Please upload data through `Upload Data` page!")
    else:

        st.markdown("### simple Wordcloud")
        # count = st.slider("Ilość słów: ", min_value=5, max_value=15)
        count = 5
        if (st.button('Reload wordcloud')):
            count = random.randint(15, 25)

        wc = generate_wordcloud.generate_wordcloud(df, count)
        st.pyplot(plot_cloud(wc))

        st.markdown("### emoji Wordcloud")

        wc_emoji = generate_emoji_wordcloud.generate_emoji_wordcloud(df)
        st.pyplot(plot_cloud(wc_emoji))
