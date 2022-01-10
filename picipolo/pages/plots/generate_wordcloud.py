from wordcloud import WordCloud
import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")
    return plt


def generate_wordcloud(df: pd.DataFrame, count: int) -> WordCloud:

    count+=3
    df = df[df['type'] == 'T']
    text = df['text'].tolist()

    words = []
    for el in text:
        el = str(el).split()
        for el2 in el:
            words.append(str(el2))

    mapka = {}
    for el in words:
        mapka.setdefault(el, 0)
        mapka[el] += 1

    res = dict(sorted(mapka.items(), key=lambda item: -item[1]))

    assert count > 0
    words_and_freq = list(res.items())[:count]

    words = ""
    for el in words_and_freq:
        words += (el[0] + " ")

    wc = WordCloud(width=3000, height=2000, background_color='salmon', colormap='Pastel1',
                          collocations=False).generate(words)
    return wc


if __name__ == '__main__':
    path = os.getcwd()+'/messengerData.csv'
    df = pd.read_csv(path, sep=';')
    
    wc = generate_wordcloud(df, 7)
    plot_cloud(wc)
