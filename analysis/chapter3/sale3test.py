#__author:iruyi
#date:2018/9/27
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt # 导入图像库
# 成功读取数据进行处理
sale = '../data/sale3.xlsx'#餐饮数据
data = pd.read_excel(sale)#读数据
print(type(data))
print(data)
print('---------------------------------')
# print(data['销量'])

data = data[(data['销量'] > 1000) & (data['销量'] < 5000)] #过滤异常数据
print('处理后：\n',data)
print(type(data))

statistics = data.describe()#保存基本统计量
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']#极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']#变异系数
statistics.loc['dis'] = statistics.loc['75%'] -statistics.loc['25%']# 四分位数间距

print(statistics)



plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.figure() #建立图像
p = data.boxplot(return_type='dict') #画箱线图，直接使用DataFrame的方法
x = p['fliers'][0].get_xdata() #'flies' 即为异常值标签
y = p['fliers'][0].get_ydata()
y.sort()#从小到大排序，该方法直接改变原对象

#用annotate添加注释
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy = (x[i],y[i]),xytext=(x[i]+0.5 - 0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i] + 0.08, y[i]))

plt.show() #展示箱线图
