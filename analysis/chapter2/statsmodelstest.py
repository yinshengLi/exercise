#__author:iruyi
#date:2018/9/27
from statsmodels.tsa.stattools import  adfuller as ADF
import numpy as np
ADF(np.random.rand(100))#返回的结果有ADF值、p值等