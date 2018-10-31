#__author:iruyi
#date:2018/10/18
import math

li = [1,3,6,4,6]
li.__setitem__(3,10)
li.insert(0,100)
print(li)


class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age

summer = chicken(2)

print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)
# 我们可以利用__class__属性找到对象的类，然后调用类的__base__属性来查询父类
print(summer.__class__.__bases__)