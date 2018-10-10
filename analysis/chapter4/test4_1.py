#__author:iruyi
#date:2018/9/28
import pandas as pd # 导入数据分析库
from scipy.interpolate import lagrange #导入拉格朗日插值函数

#  用拉格朗日法进行插补

# 成功读取数据进行处理
inputfile = '../data/chapter4_1.xlsx'#餐饮数据
outputfile = '../data/chapter4_1new.xlsx' #输出数据路径
data = pd.read_excel(inputfile)#读数据
print(type(data))
print(data)
print('---------------------------------')

# 不符合条件的数据返回None
def f(x):
    if (x < 400) | (x > 5000):
        return None
    else:
        return x

data['销量'] = data['销量'].map(lambda x: f(x))  #过滤异常值将其变为空值

print(data)


# 自定义列向量插值函数
# s 为列向量，n为被插值的位置， k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] # 取数
    y = y[y.notnull()] #提出空值
    return lagrange(y.index, list(y))(n) #插值并返回插值结果

# 诸葛元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]: #如果为空即插值
            data[i][j] = ployinterp_column(data[i],j)

data.to_excel(outputfile)
