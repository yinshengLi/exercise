#__author:iruyi
#date:2018/9/25

list = [1,5,10]
list[1] = 10

print(list)

# 元组只能读，不能修改
a = (1,2,3)
print(a[1:2])
a[1] = 10 # 赋值报错 TypeError: 'tuple' object does not support item assignment
