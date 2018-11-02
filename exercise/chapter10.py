#__author:iruyi
#date:2018/10/31
# algorithm

# top to down design

from urllib import request

web_page = request.urlopen("http://zst.aicai.com/gaopin_11ydj/5mkdzs/")
for line in web_page:
    print(line)