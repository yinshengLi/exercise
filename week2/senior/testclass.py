#__author:iruyi
#date:2018/9/21
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法 self 代表类实例
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w  # 两个下划线开头，声明该属性为私有
    #     与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例
    def speak(self):
        print('%s 说：我 %d 岁了' %(self.name, self.age))

# 单继承
class student(people):
    grade = ''
    def __init__(self ,n, a, w, g):
        # 调用父类的构造函数
        people.__init__(self,n, a, w)
        self.grade = g

#     覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))

# 多重继承
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

# 实例化类
p = people('runoob', 10, 30)
p.speak()
print("----------------------------")
s = student('ken',10,60,3)
s.speak()
print('-------------------------------multiple----')
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前的父类的方法

print('-------------------------------------------')
# 方法重写
class Parent:
    def myMethod(self):
        print('invoke parent method')

class Child(Parent):
    def myMethod(self):
        print('invoke children method')

c = Child()
c.myMethod() # 子类调用重写方法
super(Child,c).myMethod()  #用子类对象调用父类已被覆盖的方法

print('------------------------------')
# 类的私有属性
class JustCounter:
    __secretCount = 0 # __表示私有变量
    publicCount = 0 # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount) # 报错，实例不能访问私有变量
