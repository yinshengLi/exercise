#__author:iruyi
#date:2018/10/30
def fib(n):
    result = []
    a,b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return a