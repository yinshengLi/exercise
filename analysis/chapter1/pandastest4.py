#__author:iruyi
#date:2018/10/8
import pandas as pd
import numpy as np

tuples = list(zip(*[['bar','bar','baz','baz','foo','foo','qux','qux'],
                  ['one','two','one','two','one','two','one','two'] ]
))

print("tuples:\n",tuples)

index = pd.MultiIndex.from_tuples(tuples,names=['first','second'])
print('index:\n',index)

df = pd.DataFrame(np.random.randn(8,2),index=index, columns=['A','B'])
print('DataFrame:\n',df)

#The stack() method “compresses” a level in the DataFrame’s columns.
df2 = df[:4]
stacked = df2.stack()
print('stacked:\n',stacked)
print('unstacked:\n',stacked.unstack())

print('-------------------------Time Series---------------------------------------')
# rng = pd.date_range('1/1/2012', periods=100, freq='S')
# ts = pd.Series(np.random.randint(0,500, len(rng)), index= rng)
# print("time-series:\n",ts)
# print('sum:\n',ts.resample('5Min').sum())

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print("origin:\n",ts)

#Time zone representation:
ts_utc = ts.tz_localize('UTC')
print("time zone:\n",ts_utc)

# Converting to another time zone:
print('convert to another time zone:\n', ts_utc.tz_convert('US/Eastern'))

# Converting between time span representations
rng =  pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index = rng)
print('orgin:\n',ts)
ps = ts.to_period()
print(ps)
print(ps.to_timestamp())

print('------------------------------Categoricals--------------------------------------')
df = pd.DataFrame({'id':[1,2,3,4,5,6], 'raw_grade':['a', 'b', 'b', 'a', 'a', 'e']})
print(df)

df["grade"] = df["raw_grade"].astype('category')
print(df["grade"])

# Rename the categories to more meaningful name
df["grade"].cat.categories=['very good', 'good', 'very bad']
print("rename the categories:\n",df["grade"])

#Sorting is per order in the categories, not lexical order.
print('sort:\n',df.sort_values(by='grade'))

print(df.groupby("grade").size())