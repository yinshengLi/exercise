#__author:iruyi
#date:2018/9/30
import pandas as pd
original_df= pd.DataFrame({'foo': range(5), 'bar': range(5)})
print(original_df)

pd.to_pickle(original_df, '../data/dummy.pkl') # 写入文件

unpickled_df = pd.read_pickle('../data/dummy.pkl') #读取文件
print('unpickled_df:\n',unpickled_df)