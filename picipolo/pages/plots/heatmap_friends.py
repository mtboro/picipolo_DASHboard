import pandas as pd
import numpy as np
import plotly.express as px


def load_data():
    df_friends_received = pd.read_csv("data/friends.csv", delimiter=";")
    df_friends_waiting = pd.read_csv("data/friend_requests_received.csv", delimiter=";")
    df_friends_rejected = pd.read_csv("data/friend_requests_rejected.csv", delimiter=";")
    df_friends_sent = pd.read_csv("data/friend_requests_sent.csv", delimiter=";")
    return df_friends_received, df_friends_waiting, df_friends_rejected, df_friends_sent


def prepare_data():
    df_friends_received, df_friends_waiting, df_friends_rejected, df_friends_sent = load_data()
    df_friends_received["time"] = pd.to_datetime(df_friends_received['time']).dt.strftime('%Y')
    df_friends_waiting["time"] = pd.to_datetime(df_friends_waiting['time']).dt.strftime('%Y')
    df_friends_rejected["time"] = pd.to_datetime(df_friends_rejected['time']).dt.strftime('%Y')
    df_friends_sent["time"] = pd.to_datetime(df_friends_sent['time']).dt.strftime('%Y')
    df_friends_received = df_friends_received.groupby("time").size().reset_index(name='counts')
    df_friends_waiting = df_friends_waiting.groupby("time").size().reset_index(name='counts')
    df_friends_rejected = df_friends_rejected.groupby("time").size().reset_index(name='counts')
    df_friends_sent = df_friends_sent.groupby("time").size().reset_index(name='counts')
    df2 = pd.merge(df_friends_received, df_friends_waiting, on='time', how='left')
    df2.rename(columns={"counts_x": "received", "counts_y": "waiting"}, inplace=True)
    df2 = pd.merge(df2, df_friends_rejected, on='time', how='left')
    df2 = pd.merge(df2, df_friends_sent, on='time', how='left')
    df2.rename(columns={"counts_x": "rejected", "counts_y": "sent"}, inplace=True)
    df2 = df2.fillna(0)
    df2 = df2.set_index("time")
    return df2


def df_to_plotly(df):
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist()}


def create_chart():
    data = df_to_plotly(prepare_data())
    z = np.array(data.get("z"))
    z = z.T
    fig2 = px.imshow(z, labels=dict(x="Year", y="Type of friends invitation", color="Amount"), x=data.get("y"),
                     y=data.get("x"))

    return fig2

