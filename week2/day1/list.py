#__author:iruyi
#date:2018/9/17
#查询 切片查询
a=['11','22','33','44']
print(a)
print(a[0::2])
print(a[0:4:2])#步长2，从左向右
print(a[-1:-3:-1])#步长1，从右边向左
print(a[-1::-1])#步长1，从右边向左
#插入 append insert
a.append('55')
print(a)
a.insert(1,'66')
print(a)
#修改
a[1] ='xx'
print(a)
a[2:4]=['cv','dd']#修改多个值
print('after change multiple value:',a)
#删除 remove
a.remove('11')
print('after remove one element:',a)

s = a.pop(3)
print("use pop() :",s)

del a[1:3]#删除
print("after use del to delete multiple elements:",a)
del a#删除对象

#index() 找到元素的索引
ff = ['11','tht','44']
index = ff.index('tht')
print(index)

ff.reverse()
print('after use reverse() to change order:',ff)
# "+" 操作新建list， append 是修改原有的list
newff = ff + [40]
ff[0] = 12
ff.append(41)
print(ff)
print(newff)
