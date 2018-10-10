#__author:iruyi
#date:2018/9/27
from functools import reduce
a = [1, 2, 3]
# 列表解析
b = [x+2 for x in a]
print('a: ', a)
print('b: ', b)
# map() 函数 map()函数效率比列表解析效率更高
c = map(lambda x: x+2, a)
print('c: ', list(c))
d = map(lambda x, y:x*y, a, b)
print('d: ', list(d))

# reduce()递归
# 4的阶乘
n = reduce(lambda x,y:x*y,range(1,5))
print('n: ', n)
# 循环表示
aa = 1
for i in range(1,5):
    aa *= i
print('aa: ', aa)

# filter() 过滤
e = filter(lambda x: x>2 and x<8, range(10))
print('e: ', list(e))
# 解析表示过滤
f = [i for i in range(10) if i>2 and i<8]
print('f: ', f)