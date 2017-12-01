''' 进阶篇
类的成员 字段 方法和属性
字段 普通字段 静态字段
方法 普通方法 类方法 静态方法
属性 普通属性
'''
'''
class Province:
    #静态字段
    country='中国'

    def __init__(self,name):
        #普通字段
        self.name=name

#直接访问普通字段
obj=Province('河北省')
print(obj.name)
#直接访问静态字段
print(Province.country)
'''

'''
方法 普通方法 类方法 静态方法

'''
'''
class Foo:
    def __init__(self,name):
        self.name=name

    def ord_func(self):
        print("普通方法")

    @classmethod
    def class_func(cls):
        #定义类方法，至少有一个cls参数
        print('类方法')

    @staticmethod
    def static_func():
        '''定义静态方法,无默认参数'''
        print("静态方法")

#调动普通方法
f=Foo("你好")
f.ord_func()

#调用类方法
Foo.class_func()

#调用静态方法
Foo.static_func()
'''

'''
属性的基本使用
属性的两种定义方式
'''
# ############### 定义 ###############
class Pager:
    def __init__(self, current_page):
        self.current_page = current_page  #用户当前请求的页码（第一页、第二页...)      
        self.per_items = 10  #每页默认显示10条数据
    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val
    @property
    def end(self):
        val = self.current_page * self.per_items
        return val
    
    # ############### 调用 ###############
    p = Pager(1)
    p.start #就是起始值，即：m
    p.end #就是结束值，即：n



















        
