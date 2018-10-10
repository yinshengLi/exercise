#__author:iruyi
#date:2018/9/25
import time
# 获取秒
ticks = time.time()
print('当前时间为：', ticks)

# 获取本地时间
localtime = time.localtime(ticks)
print('本地时间为：', localtime)

# 获取格式化的时间 Tue Sep 25 15:34:36 2018
formattime = time.asctime(localtime)
print('本地时间为：', formattime)

# 格式化日期
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
#



# 格式化成 2018-09-25 15:34:36 形式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 格式化成 Tue Sep 25 15:34:36 2018 形式
print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))

# 是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）
print(time.timezone)
