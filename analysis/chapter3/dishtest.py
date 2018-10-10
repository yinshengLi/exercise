# -*- coding=utf-8 -*-
#__author:iruyi
#date:2018/9/27
from __future__ import print_function
import pandas as pd
# 菜品盈利帕累托图代码
# 初始化参数
dishprifit = '../data/dish_profit.xlsx'#餐饮数据
data = pd.read_excel(dishprifit)#读数据u
data = data['盈利'].copy()
# data = sorted(data,reverse = False)
print(type(data))
print(data)
print('---------------------------------')
data = pd.DataFrame(data)
print(type(data))

import matplotlib.pyplot as plt #导入图像库
plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.figure() #建立图像

data.plot(kind='bar')
plt.ylabel('盈利（元）')
p = 1.0*data.cumsum()/data.sum()
p.plot(color ='r', secondary_y = True, style = '-o', linewidth = 2)
print("------------------------------------")
f = p['盈利'][6]
plt.annotate(format(f, '.4%'), xy = (6, f), xytext=(6*0.9, f*0.9),
             arrowprops = dict(arrowstyle='->', connectionstyle='arc3,rad=.2')) # 添加注释，即85%处的标记，这里包括了指定箭头样式
plt.ylabel('盈利（比例）')
plt.show()


