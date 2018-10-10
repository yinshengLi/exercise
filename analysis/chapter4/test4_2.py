#__author:iruyi
#date:2018/9/28
import pandas as pd
import numpy as np

#  数据规范化

inputfile = '../data/normalization4_2.xlsx' #输出数据路径

data = pd.read_excel(inputfile, header=None) #读取数据
print('----------------最小-最大规范化---------------------')
print((data-data.min())/(data.max() - data.min())) #最小-最大规范化
print('----------------------零-均值规范化-------------------------')
print((data-data.mean())/data.std()) #零-均值规范化
print('-------------------小数定标规范化----------------------------')
print(data/10**np.ceil(np.log10(data.abs().max()))) #小数定标规范化