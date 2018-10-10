#__author:iruyi
#date:2018/9/21
import re

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

#match re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
line = 'This is a wonderful world'
tt = re.match(r'(.*) is a (.*)', line)
if tt:
    print('all is :', tt.group())
    print('first is :', tt.group(1))
    print('second is :', tt.group(2))
else:
    print('no matches')

#search re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
ff = re.search(r'(.*) is a (.*)',line)
if ff:
    print('all is :', ff.group())
    print('first is :', ff.group(1))
    print('second is :', ff.group(2))
else:
    print('no matches')

# sub 用于替换字符串中的匹配项
phone = '2004-959-559#这是一个字符串'
#删除注释
num = re.sub(r'#.*$', '', phone)
print('number is :', num)
print('phone:', phone)

#移除非数字内容
num = re.sub(r'\D', '', phone)
print('number is :', num)
print('phone:', phone)

# compile
# findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
pattern = re.compile(r'\d+')#查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('runoob88bd3df98dd0')
print('result1:', result1)
print('result2:', result2)

# finditer 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r'\d+', 'dd45ddff45dd90')
for match in it:
    print(match.group())
