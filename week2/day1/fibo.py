#__author:iruyi
#date:2018/9/12

def fib(n):
    a,b = 0,1
    while a < n:
        print(a,end=' ')
        a,b=b,a+b
    print()

def fib2(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result

#解释器执行 python fibo.py 50
# By this it can be executed directly,also can be imported as a module
# this likes main() in java ,you can use it to test your program
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

