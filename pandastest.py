import pandas as pd
#d=pd.Series(range(20))
#print(d)

a=pd.Series([9,8,7,6])
print(a)
#
b=pd.Series([9,8,7,6],index=['a','b','b','d'])
print(b)
#标量方式
s=pd.Series(25,index=['a','b','b','d'])
print(s)
#字典方式
d=pd.Series({'a':9,'b':8,'c':7})
print(d)
e=pd.Series({'a':9,'b':8,'c':7},index=['c','a','b','d'])
print(e)

import numpy as np
n=pd.Series(np.arange(5))
print(n)

m=pd.Series(np.arange(5),index=np.arange(9,4,-1))
print(m)

print(b.index)
print(b.values)
