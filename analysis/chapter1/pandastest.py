#__author:iruyi
#date:2018/9/29

import pandas as pd

df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]})
print(type(df))
print(df)
print('------if-then on one column----------')
df.loc[df.AAA >=5,'BBB'] = -1 # 如果AAA >=5 ,把对应的BBB改为-1
print(df)

print('---if-then with assignment to 2 columns----')
df.loc[df.AAA >=5, ['BBB', 'CCC']] = 555
print(df)

print('-----------use pandas where after you’ve set up a mask---------------')
df_mask = pd.DataFrame({'AAA':[True]*4,'BBB':[False]*4, 'CCC':[True,False]*2})
print(df_mask)
print(df.where(df_mask,-1000)) # df中的值对应df_mask中值是true，显示df值，false则显示-1000


