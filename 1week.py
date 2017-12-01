"""
#计算 1+2!+3!+...+10!的结果

sum,tmp=0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp

print("运行结果是:{}".format(sum))
"""

"""
猴子第一天摘下若干个桃子，当即吃了一半，还
不过瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多
吃了一个。以后每天早上都吃了前一天剩下的一半多一个。到第五天
早上想再吃时，见只剩下一个桃子了。请编写程序计算猴子第一天共
摘了多少桃子。
"""
"""
n=1
for i in range(5,0,-1):
    n=(n+1)<<1
print(n)

"""

"""
#五角星
from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
end_fill()

"""
"""
#太阳花
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
 forward(200)
 left(170)
 if abs(pos()) < 1:
     break
end_fill()
done() 
"""

"""
#绘制一个螺旋线的图形
import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
 turtle.forward(2*x)
 turtle.left(90)
time.sleep(3) 
"""

"""
#
import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow",'purple','blue']
turtle.tracer(False)
for x in range(400):
 turtle.forward(2*x)
 turtle.color(colors[x % 4])
 turtle.left(91)
turtle.tracer(True)
"""









