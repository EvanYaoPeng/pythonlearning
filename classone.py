#封装 继承 多态(不支持)
'''
class Foo:
    def Bar(self):
        print("Bar")

    def Hello(self,name):
        print("i am ",name)

obj=Foo()
obj.Bar()
obj.Hello('evan')
'''
'''
#封装
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name)
        print(self.age)

obj1 = Foo('wupeiqi', 18)
print(obj1.name) # 直接调用obj1对象的name属性
print(obj1.age) # 直接调用obj1对象的age属性
print(obj1.details()) #self间接调用封装内容
obj2 = Foo('alex', 73)
print(obj2.name) # 直接调用obj2对象的name属性
print(obj2.age) # 直接调用obj2对象的age属性
print(obj2.details()) #self间接调用封装内容
'''

'''
1、创建三个游戏人物，分别是：
苍井井，女，18，初始战斗力1000
东尼木木，男，20，初始战斗力1800
波多多，女，19，初始战斗力2500
2、游戏场景，分别：
草丛战斗，消耗200战斗力
自我修炼，增长100战斗力
多人游戏，消耗500战斗力

作者： IT程序狮 
链接：http://www.imooc.com/article/2925
来源：慕课网
'''

# -*- coding:utf-8 -*- # ##################### 定义实现功能的类 ##################### 
class Person: 
	def __init__(self, na, gen, age, fig): 
		self.name = na 
		self.gender = gen 
		self.age = age 
		self.fight =fig 
	def grassland(self): 
		"""注释：草丛战斗，消耗200战斗力""" 
		self.fight = self.fight - 200 
	def practice(self): 
		"""注释：自我修炼，增长100战斗力""" 
		self.fight = self.fight + 100 
	def incest(self): 
		"""注释：多人游戏，消耗500战斗力""" 
		self.fight = self.fight - 500 
	def detail(self): 
		"""注释：当前对象的详细情况""" 
		temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight) 
		print(temp)
# ##################### 开始游戏 ##################### 
cang = Person('苍井井', '女', 18, 1000) # 创建苍井井角色 
dong = Person('东尼木木', '男', 20, 1800) # 创建东尼木木角色 
bo = Person('波多多', '女', 19, 2500) # 创建波多多角色 
cang.incest() #苍井空参加一次多人游戏 
dong.practice()#东尼木木自我修炼了一次 
bo.grassland() #波多多参加一次草丛战斗 #输出当前所有人的详细情况 
cang.detail() 
dong.detail() 
bo.detail() 
cang.incest() #苍井空又参加一次多人游戏 
dong.incest() #东尼木木也参加了一个多人游戏 
bo.practice() #波多多自我修炼了一次 #输出当前所有人的详细情况 
cang.detail() 
dong.detail() 
bo.detail() #游戏人生


#继承
class Animal: 
	def eat(self): 
		print("%s 吃 " %self.name )
	def drink(self): 
		print("%s 喝 " %self.name )
	def shit(self): 
		print( "%s 拉 " %self.name )
	def pee(self): 
		print( "%s 撒 " %self.name )

class Cat(Animal): 
	def __init__(self, name): 
	    self.name = name 
	    self.breed='猫' 
	def cry(self): 
	    print('喵喵叫')
		
class Dog(Animal): 
	def __init__(self, name): 
	    self.name = name 
	    self.breed = '狗' 
	#def cry(self):
           # print('汪汪叫')
                
# ######### 执行 ######### 
c1 = Cat('小白家的小黑猫') 
c1.eat()

c2 = Cat('小黑的小白猫') 
c2.drink()

d1 = Dog('胖子家的小瘦狗') 
d1.eat()


'''
1、Python的类可以继承多个类，Java和C#中则只能继承一个类
2、Python的类如果继承了多个类，那么其寻找方法的方式有两种，分别是：深度优先和广度优先
深度优先 经典类继承时
广度优先 新式类继承时 继承自object 就是新式类
'''
'''经典类继承时 深度优先
class D:
    def bar(self):
        print(D.bar')
class C(D):
    def bar(self):
        print('C.bar')
class B(D):
    def bar(self):
        print('B.bar')
class A(B, C):
    def bar(self):
        print(A.bar')

a = A()
      # 执行bar方法时
      # 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错
      # 所以，查找顺序：A --> B --> D --> C # 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

'''

''' 就是新式类 广度优先
class D(object):
    def bar(self):
        print 'D.bar'
class C(D):
    def bar(self):
        print('C.bar')
class B(D):
    def bar(self):
        print('B.bar')
class A(B, C):
    def bar(self):
        print(A.bar')

a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

#在上述查找过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
'''

