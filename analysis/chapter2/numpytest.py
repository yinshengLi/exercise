#__author:iruyi
#date:2018/9/27
import numpy as np
# numpy 提供数组/多维数组功能 http://www.numpy.org/
list = [2, 0, 1, 5]
a = np.array(list)
print(list)
print('a:\n',a)
print(a[:3])
print(a.min())
a.sort()
print('sorted:\n',a)
print(a[1])

b = np.array([[1,2,3],[4,5,6]])#创建二维数组
print('tow-dimensional array:\n',b)
print(b[1][0])
print(b*b)