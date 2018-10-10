#__author:iruyi
#date:2018/9/28
from __future__ import print_function
import pandas as pd
import numpy as np

# 餐饮销量数据相关性分析
sale = '../data/sale_all.xlsx'#餐饮数据
data = pd.read_excel(sale, index_col='日期')#读数据
print(type(data))
print(data)
print('---------------------------------')

print(data.corr()) #相关系数矩阵，即给出了任意两款菜式之间的相关系数


# print("-------------------------------")
# print(data.corr()['A1']) #只显示A1与其它菜式的相关系数

# print("-------------------------------")
# print(data['A1'].corr(data['A2'])) #计算A1 与 A2的相关系数
#
#
print("----------------采用 Spearman方法------------------")
D = pd.DataFrame([range(1,8), range(2,9)])
print(D)
print("-----")
D.corr(method='pearson') #计算相关系数矩阵
S1 = D.loc[0] #提取第一行
S2 = D.loc[1] # 提取第二行
f = S1.corr(S2, method='pearson') #计算S1、S2的相关系数
print(f)

print("-----------协方差矩阵--------------------------")
H = pd.DataFrame(np.random.randn(6,5)) #产生6x5随机矩阵
print(H)
H.cov() #计算协方差矩阵
print(H[0].cov(H[1])) #计算第一列和第二列的协方差
