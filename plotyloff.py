#https://plot.ly/python/
import plotly.plotly
import plotly.graph_objs as go

trace = go.Box(
    x=[1, 2, 3, 4, 5, 6, 7]
)
data = [trace]
plotly.offline.plot(data) 
