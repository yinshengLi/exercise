#__author:iruyi
#date:2018/10/30

lista = ['a', 'b', 'c']
for i in enumerate(lista): # 返回键值对 key 对应索引
    print(i)

# 对list 值翻倍处理
for pair in enumerate(lista): # 返回键值对 key 对应索引
    i = pair[0]
    v = pair[1]
    lista[i] = 2*v
print(lista)
# 或者
for (i, v) in enumerate(lista):
    lista[i] = 2*v
print(lista)
