#__author:iruyi
#date:2018/10/8
import tushare as tu
import pandas as pd

token='8f4b0cb38851c06e5a2e52e1ccfdf16cb473adb1ca1ff5afea509c96' #调用接口token
tu.set_token(token)# 设置token
pro = tu.pro_api() # 初始化pro接口

# data = tu.get_index()
# df = pd.DataFrame(data)
#
# outputfile = '../data/finance.xlsx' #输出数据路径
# df.to_excel(outputfile)
# print("结束")

print('------------------------查询股票列表----------------------------------------')
# 入参
'''
is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
list_status	str	N	上市状态 L上市 D退市 P暂停上市
exchange_id	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所
'''
# 出参
'''
ts_code	str	TS代码
symbol	str	股票代码
name	str	股票名称
fullname	str	股票全称
enname	str	英文全称
exchange_id	str	交易所代码 SSE上交所 SZSE深交所 HKEX港交所
curr_type	str	交易货币
list_status	str	上市状态 L上市 D退市 P暂停上市
list_date	str	上市日期
delist_date	str	退市日期
is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
'''
# st = pro.query('stock_basic', exchange_id='', is_hs='S', fields='ts_code,symbol,name,list_date,list_status')
# st.to_excel('../data/finance2.xlsx')
# print(st)

print('---------------------------查询日线行情--------------------------------------')
# 入参
'''
ts_code	str	N	股票代码（二选一）
trade_date	str	N	交易日期（二选一）
start_date	str	N	开始日期
end_date	str	N	结束日期
'''
#出参
'''
ts_code	str	股票代码
trade_date	str	交易日期
open	float	开盘价
high	float	最高价
low	float	最低价
close	float	收盘价
pre_close	float	昨收价
change	float	涨跌额
pct_change	float	涨跌幅
vol	float	成交量 （手）
amount	float	成交额 （千元）
'''
# daily = pro.query('daily', ts_code='000001.SZ', start_date='20180901',end_date='20181009')
# daily.to_excel('../data/daily.xlsx')
# print(daily)

print('--------------------------停复牌信息-------------------------------------')
#入参
'''
ts_code	str	N	股票代码(三选一)
suspend_date	str	N	停牌日期(三选一)
resume_date	str	N	复牌日期(三选一)
'''
# 出参
'''
ts_code	str	股票代码
suspend_date	str	停牌日期
resume_date	str	复牌日期
ann_date	str	公告日期
suspend_reason	str	停牌原因
reason_type	str	停牌原因类别
'''
# suspend = pro.query('suspend', ts_code='', suspend_date='20181009', resume_date='',fields='')
# print(suspend)

print('------------------------------每日指标-------------------------------')
# 入参
'''
ts_code	str	Y	股票代码（二选一）
trade_date	str	N	交易日期 （二选一）
start_date	str	N	开始日期
end_date	str	N	结束日期
'''
#出参
'''
ts_code	str	TS股票代码
trade_date	str	交易日期
close	float	当日收盘价
turnover_rate	float	换手率
volume_ratio	float	量比
pe	float	市盈率（总市值/净利润）
pe_ttm	float	市盈率（TTM）
pb	float	市净率（总市值/净资产）
ps	float	市销率
ps_ttm	float	市销率（TTM）
total_share	float	总股本 （万）
float_share	float	流通股本 （万）
free_share	float	自由流通股本 （万）
total_mv	float	总市值 （万元）
circ_mv	float	流通市值（万元）
'''
daily_basic = pro.query('daily_basic', ts_code='', trade_date='20180723')
daily_basic.to_excel('../data/daily_basic.xlsx')
print(daily_basic)