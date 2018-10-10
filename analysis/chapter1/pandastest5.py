#__author:iruyi
#date:2018/10/8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

plt.show()

# On a DataFrame, the plot() method is a convenience to plot all of the columns with labels:
df = pd.DataFrame(np.random.randn(1000,4), index = ts.index, columns=['A','B','C','D'])
print('orgin:\n',df)
df = df.cumsum()
print('solved:\n',df)
df.plot()
plt.legend(loc='best')
plt.show()