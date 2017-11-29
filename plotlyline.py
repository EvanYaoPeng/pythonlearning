import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('DemoAccount', '2qdyfjyr7o') # 注意：这里是plotly网站的用户名和密码

trace = go.Bar(x=[2, 4, 6], y= [10, 12, 15])
data = [trace]
layout = go.Layout(title='A Simple Plot', width=800, height=640)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='a-simple-plot.png')

from IPython.display import Image
Image('a-simple-plot.png')
