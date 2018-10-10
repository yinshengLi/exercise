#__author:iruyi
#date:2018/9/29
#逻辑回归 自动建模
# 当数据量太少时，会报错 valueError: This solver needs samples of at least 2 classes in the data, but the data contains only one class: 0
import pandas as pd

#参数初始化
datafile = '../data/loan_default.xlsx'
data = pd.read_excel(datafile) # 读取数据
print(type(data))
print('---------------------------')
x = data.iloc[:, :8].values
y = data.iloc[:, 8].values
print('x:\n',x)
print('y:\n',y)
print('-----------------------------------------------')
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
rlr =  RLR() #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y) #训练模型
xx = rlr.get_support() #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
print(xx)
print('通过随机逻辑回归模型筛选特征结束。')
print('有效特征为：%s' % ','.join(data.columns[rlr.get_support(indices=True)]))

x = data[data.columns[rlr.get_support(indices=True)]]

lr = LR() #建立逻辑货柜模型
lr.fit(x,y) #用筛选后的特征数据来寻来模型
print('逻辑回归模型训练结束')
print('模型的平均正确率为：%s' % lr.score(x,y)) #给出模型的平均正确率，本例为81.4%