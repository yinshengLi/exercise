#__author:iruyi
#date:2018/9/29
import numpy as np
import pandas as pd

# unique
D = pd.Series([1, 1, 4, 3, 5])
print(D.unique())
print(np.unique(D)) #np.unique() 参数是以为数组，可以是list,array,Series
print('-----------------------------------------')
#isnull() 和 notnull()
F = pd.Series([1, 1, 4, 3, 5, None])
print(F)
F1 = F[F.notnull()]
F2 = F[F.isnull()]
print(F1)
print('-----------------------------------------')

#random   np.random.rand(k,m,n,.....) 生成k x m x n x .....随机矩阵
k = np.random.rand(3, 4,5) #生成3x4x5 随机矩阵，元素均匀分布在（0,1）上
print(k)
print('---------randn--------------------------------')
j = np.random.randn(3,4) #生成3x4随机矩阵，元素服从标准正太分布
print(j)

print('-----------------------------------------')