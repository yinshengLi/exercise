#__author:iruyi
#date:2018/9/28
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# print("------------二维线图-------------------")
# plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
# plt.figure() #建立图像
#
# x = np.linspace(0,2*np.pi, 50) # x坐标输入
# y = np.sin(x) #计算对应x 的正弦值
# plt.plot(x,y, 'bp--') # 控制图形格式为蓝色带星虚线，显示正弦曲线
# plt.show()


print('------------------pie 饼图-------------------')
labels = ('Frogs', 'Hogs', 'Dogs', 'Logs') #定义标签
sizes = [15, 30, 45, 10] #每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'] #每一块的颜色
explode = (0, 0.1, 0, 0) #突出显示，这里仅仅突出显示第二块

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal') #显示为圆（避免比例压缩为椭圆形）
plt.show()

#
# print('------------------直方图-------------------')
# x = np.random.randn(1000) # 1000 个服从正太分布的随机数
# print(x) # 列表
# plt.hist(x, 10) #分成10组进行绘制直方图
# plt.show()

# print('--------------------box 箱型图-----------------------------------')
# D = pd.DataFrame([x, x+1]).T #构造两列的DataFrame
# D.plot(kind='box') #调用Series内置的作图方法画图，用kind参数指定箱形图box
# plt.show()

# print('---------------------绘制x轴或者y轴的对数图----------------------------------------')
# x = pd.Series(np.exp(np.arange(20))) #原始数据
# x.plot(label = '原始数据图', legend = True)
# plt.show()
# x.plot(logy = True, label = '对数数据图', legend = True)
# plt.show()

print('----------------------------误差图------------------------------------')
error = np.random.randn(10) #定义误差列
print(error)
y = pd.Series(np.sin(np.arange(10))) #均值数据列
y.plot(yerr = error) #绘制误差图
plt.show()

