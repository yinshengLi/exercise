#__author:iruyi
#date:2018/10/18
import tushare as tu
import pandas as pd

token='8f4b0cb38851c06e5a2e52e1ccfdf16cb473adb1ca1ff5afea509c96' #调用接口token
tu.set_token(token)# 设置token
pro = tu.pro_api() # 初始化pro接口