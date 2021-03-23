import pandas as pd
import plotly.express as px

df = pd.read_csv("py2/data/coffee vs hours of sleep.csv")

fig = px.scatter(df,x= "Coffee in ml", y = "sleep in hours")
fig.show()
