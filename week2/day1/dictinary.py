#__author:iruyi
#date:2018/9/17
#格式化
table={'ss':321,'kk':33,"55p":99}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels不知道'
print(f'My hovercraft is full of {animals}')
print(f'test !s means {animals !s}')#'!s' applies str()
print(f'test !a means {animals !a}')# '!a' applies ascii()
print(f'test !r means {animals !r}')#'!r' applies repr()
