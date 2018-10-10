# __author:iruyi
# date:2018/9/30

import pandas as pd
import numpy as np

print('-------------Setting a new column automatically aligns the data by the indexes.-------')
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
s2 = pd.Series([1, 2, 3, 4, 5, 6])
print(s1)
print(s2)

dates = pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
# print("-------Setting values by label:-----")
# df.at[dates[0],'A'] = 0
# print(df)
# print('---------Setting values by position-------')
# df.iat[0,1] = 0
# print(df)
# print("length:", len(df))
# print('-------Setting by assigning with a NumPy array---------')
# df.loc[:,'D'] = np.array([5] * len(df))
# print(df)

# print('-------A where operation with setting-----')
# df2 = df.copy()
# print(df2[df2>0])
# df2[df2 > 0] = -df2
# print(df2)

print('------------------------Missing Data------------------------------------------')
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print('df1:\n', df1)

print('------------------To drop any rows that have missing data.----------------------')
print(df1.dropna(how='any'))
#
print('----------Filling missing data.------------')
print(df1.fillna(value=5))
#
print('--------To get the boolean mask where values are nan-------------')
print(pd.isna(df1))

print('-------------########################------Operation-------#####################--')
print(df.mean())  # 计算每一列的平均值
print('param:\n', df.mean(1))  # 计算每一行的平均值

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)
print(s)
print('shift:\n', s.shift(2))  # 值下移，上面的值用Nan 填充
#
print(df.sub(s, axis='index'))

print("---------------------------String Methods------------------------------------------")

s = pd.Series(['A','B','C','Aaba', 'Baca',np.nan,'CBAD'])

print(s.str.lower())
