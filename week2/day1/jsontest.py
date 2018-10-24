#__author:iruyi
#date:2018/9/19
import json

f = json.dumps([1, 'simple', 2])
print(type(f))
file1 = open("C:/WorkspacePython/testfile.txt", 'w+')
file1.write(f)
file1.close()

file2 = open("C:/WorkspacePython/testfile.txt", 'r')
x = json.load(file2)
file2.close()
print(type(x))

# 检测类型两种方式
if type(x) == list:
    print('true')

if isinstance(x, list):
    print('true')

