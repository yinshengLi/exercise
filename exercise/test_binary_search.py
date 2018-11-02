#__author:iruyi
#date:2018/11/2
import nose
from exercise import chapter11_2 as bs

# The list to search with.
VALUES = [1, 3, 4, 5, 7, 9, 10]
def test_first():
    '''Test a value at the beginning of the list.'''
    assert bs.binary_search(1, VALUES) == 0

def test_duplicate():
    '''Test a duplicate value.'''
    assert bs.binary_search(4, VALUES) == 2

def test_middle():
    '''Test searching for the middle value.'''
    assert bs.binary_search(5, VALUES) == 4


def test_last():
    '''Test searching for the last value.'''
    assert  bs.binary_search(10, VALUES) == 7

if __name__ == '__main__':
    nose.run()
