import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 
df = pd.read_csv("parsed_data.csv", delimiter = ";")
df.rename(columns={"2021.12.12" : "data", "19:27:28" : "godzina", "Jakub Stolarczyk" : "uzytkownik", "Fu" : "wiadomosci"}, inplace=True)
df = df.groupby("data").size().reset_index(name='counts')
df['cumsum'] = df['counts'].cumsum()
df = df[["data","cumsum"]]
df['data']= pd.to_datetime(df['data']).dt.strftime('%Y-%m-%d')
#generating plot 
trace1 = go.Scatter(x=df['data'][:2],
                    y=df['cumsum'][:2],
                    fill='tozeroy'
                    )
frames = [dict(data= [dict(type='scatter',
                           x=df['data'][:k+1],
                           y=df['cumsum'][:k+1]),

                     ],
               traces= [0],  
              )for k  in  range(1, len(df)-1)]
layout = go.Layout(width=700,
                   height=600,
                   showlegend=False,
                   hovermode='x unified',
                   updatemenus=[
                        dict(
                            type='buttons', showactive=False,
                            y=1.05,
                            x=1.15,
                            xanchor='right',
                            yanchor='top',
                            pad=dict(t=0, r=10),
                            buttons=[dict(label='Play',
                            method='animate',
                            args=[None, 
                                  dict(frame=dict(duration=2, 
                                                  redraw=False),
                                                  transition=dict(duration=0),
                                                  fromcurrent=True,
                                                  mode='immediate')]
                            )]
                        ),
                        dict(
                            type = "buttons",
                            direction = "left",
                            buttons=list([
                                dict(
                                    args=[{"yaxis.type": "linear"}],
                                    label="LINEAR",
                                    method="relayout"
                                ),
                                dict(
                                    args=[{"yaxis.type": "log"}],
                                    label="LOG",
                                    method="relayout"
                                )
                            ]),
                        ),
                    ]              
                  )
layout.update(title = "How many messeges with your friend",
              xaxis =dict(range=['2013-04-02', '2021-12-12'], autorange=False),
              yaxis =dict(range=[0, max(df["cumsum"])], autorange=False));
fig = go.Figure(data=[trace1], frames=frames, layout=layout)
fig.show()