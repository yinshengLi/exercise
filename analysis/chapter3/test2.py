#__author:iruyi
#date:2018/9/27
from __future__ import print_function
import pandas as pd

sale = '../data/sale.xlsx'#餐饮数据
data = pd.read_excel(sale, index_col='时间')#读数据,指定时间为索引列
print(type(data))
print(data)
print('---------------------------------')
# print(data.loc['销量'] > 400)

# data = data[(data['销量'] > 400) & (data['销量'] < 5000)] #过滤异常数据 ,书中例子无法正常运行
data = data.loc[:, (data.loc['销量'] > 400) & (data.loc['销量'] < 4000)] #过滤异常数据
print(data)

statistics = data.describe()#保存基本统计量
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']#极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']#变异系数
statistics.loc['dis'] = statistics.loc['75%'] -statistics.loc['25%']# 四分位数间距

print(statistics)
