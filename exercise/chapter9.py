#__author:iruyi
#date:2018/10/31
ten = set(range(10))

lows = set([0, 1, 2, 3, 4])
odds = set([1, 3, 5, 7, 9])
lows.add(9)
print("ten:", ten)
print("low:", lows)

print('difference:', lows.difference(odds))
print('intersection', lows.intersection(odds))

print('issubset:', lows.issubset(ten))
print('issuperset:', lows.issuperset(odds))

lows.remove(1)
print(lows)

print('union:', lows.union(odds))
