#__author:iruyi
#date:2018/11/2
import time
from exercise import chapter11

def time_it(search, v, L):
    '''Time how long it takes to run function search to find value v in list L.'''
    t1 = time.time()
    search(v, L)
    t2 = time.time()
    return (t2 - t1) * 1000

def print_times(v, L):
    ''' Print the number of milliseconds it takes for linear_search(v,L) to run
    for list.index, basic linear serch, the for loop linear search, and sentinel search.'''

    #Get list.index's running time.
    t1 = time.time()
    L.index(v)
    t2 = time.time()
    index_time = (t2 - t1) * 1000

    # Get the other three running times.
    basic_time = time_it(chapter11.linear_search, v, L)
    for_time = time_it(chapter11.linear_search2, v, L)
    sentinel_time = time_it(chapter11.linear_search3, v, L)

    print("value=%d\t basic_time=%.02f\t for_time=%.02f\t sentinel_time=%.02f\t index_time=%.02f"
          % (v, basic_time, for_time, sentinel_time, index_time))



L = list(range(1000001))
chapter11.linear_search(10, L)
print_times(10, L)
print_times(500000, L)
print_times(1000000, L)
