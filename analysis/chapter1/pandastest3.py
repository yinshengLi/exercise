#__author:iruyi
#date:2018/9/30
import pandas as pd
import numpy as np

print('-----------------------Merge------------------------------')

print('----------------concat-------')
df = pd.DataFrame(np.random.randn(10,4))
print('df:\n',df)

pieces = [df[:3],df[3:7],df[7:]]
print(pd.concat(pieces))

print('----------Join----------')
left = pd.DataFrame({'key':['foo','foo'], 'lval':[1,2]})
right = pd.DataFrame({'key':['foo','foo'],'rval':[4,5]})
print('left:\n',left)
print('right:\n',right)
print(pd.merge(left,right,on='key')) # 4条数据

left = pd.DataFrame({'key':['foo','bar'], 'lval':[1,2]})
right = pd.DataFrame({'key':['foo','bar'],'rval':[4,5]})
print('left:\n',left)
print('right:\n',right)
print(pd.merge(left,right,on='key')) #key 相同，把对应的值合并 2条数据

print('----------------------Append----------------')
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]
print(df.append(s, ignore_index=True)) # s 被添加到末尾

print('------------------------Grouping---------------------')
df = pd.DataFrame({
    'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
    'B':['one','one','two','three','two','two','one','three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})

print(df)
print('grouping:\n', df.groupby('A').sum())
print('grouping:\n', df.groupby(['A', 'B']).sum()) #按照A、B分组



