import pandas as pd
dl={'城市':['北京','上海','广州','深圳','沈阳'],
'环比':[101.5,101.2,101.3,102.0,100.1],
'同比':[120.7,127.3,119.4,140.9,101.4],
'定基':[121.4,127.8,120.0,145.5,101.6]}
'''
d=pd.DataFrame(dl,index=['c1','c2','c3','c4','c5'])
print(d)
d=d.reindex(index=['c5','c4','c3','c2','c1'])
print(d)
d=d.reindex(columns=['城市','环比','同比','定基'])
print(d)
'''

d=pd.DataFrame(dl)
print(d.columns)
print(d.index)
print(d.row)
