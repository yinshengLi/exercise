#__author:iruyi
#date:2018/9/29
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print('--------###############-----Series-----------#############----------')
# s = pd.Series([1, 3, 4, np.nan, 6, 8])
# print(s)
# print(s[0])
#
#
print('---------#################------DataFrame----------##################-------------')
# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns
dates = pd.date_range('20130101', periods=6)
# print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
# df2 = pd.DataFrame({
#     'A': 1.,
#     'B': pd.Timestamp('20130102'),
#     'C': pd.Series(1, index=list(range(4)),dtype='float32'),
#     'D': np.array([3]*4, dtype='int32'),
#     'E': pd.Categorical(['test', 'train','test','train']),
#     'F': 'foo'
# })
# print('df2:\n',df2)
# print('df2-types:\n',df2.dtypes)
#
# print('-------------Here is how to view the top and bottom rows of the frame:------------')
# print('head:\n', df.head(3))
# print('tail:\n',df.tail(3))



# print('------------Display the index, columns, and the underlying NumPy data:----------')
# print('index:\n', df.index)
# print('columns:\n', df.columns)
# print('values:\n', df.values)
#
# print('-----------describe() shows a quick statistic summary of your data:---------')
# print(df.describe())

# print('-------------Transposing your data:----------------')
# print(df.T) #行变列，列变行
# print('--------------Sorting by an axis:--------')
# print(df.sort_index(axis=1, ascending=False))

#Selection
print('#####################-----------Selection-----------###############################----')
 # df['A'] Selecting a single column, which yields a Series, equivalent to df.A:
# print(df['A'])
# print(df.A)

# print('-------------dSelecting via [], which slices the rows.---------------')
# print('slice three rows:\n', df[0:3])
#
# print('-------------For getting a cross section using a label:---------------')
# print(dates[0])
# print(df.loc[dates[0]]) # equeals get
#
# print('----------Selecting on a multi-axis by label-------')
# print(df.loc[:, ['A','B']])
# print(df.loc['20130102':'20130104',['A', 'B']])

# print(df.loc['20130102',['A','B']])
# print(df.loc['20130102',['A','B']].A)
# print(df.loc['20130102',['A','B']]['A'])
#
#
# # Selection by Position
#
# print('--------###############------Selection by Position---------################-------------')
# print(df)
# print(df.iloc[3])
# print(df.iloc[0:3, 0:2])
# print(df.iloc[[1, 3, 4], [1, 2]]) # By lists of integer position locations, similar to the numpy/python style:
# print(df.iloc[1:3, :]) # For slicing rows explicitly
# print(df.iloc[:, 1:3]) # For slicing columns explicitly
# print(df.iloc[1, 1]) # For getting a value explicitly
#
# print('--------For getting fast access to a scalar (equivalent to the prior method)----------')
# print(df)
# print(df.iat[1,1])

# print('----------###############-------------Boolean Indexing---------###################---------')
# print(df[df.A > 0]) # Using a single column’s values to select data.
# print(df > 0)
# print('boolean index:\n',df[df > 0]) # Selecting values from a DataFrame where a boolean condition is met

print('-----------Using the isin() method for filtering:----')
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2['E'].isin(['two','four'])])