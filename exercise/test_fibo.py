#__author:iruyi
#date:2018/10/30
import nose
import exercise.modulefibo as ff

def test_fibo():
    ''' test fibo'''
    print("start")
    assert ff.fib(10) == 13, "it is wrong"


# debug can access but direct run can not access in pycharm
if __name__ == '__main__':
    print("----ss------")
    nose.run()