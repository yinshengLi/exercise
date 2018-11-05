#__author:iruyi
#date:2018/11/5
import bisect
import time

# 高效排序算法
def bin_sort(values):
    ''' Sort values, creating  a new list.'''
    result = []
    for v in values:
        bisect.insort_left(result, v)
    return result

# 合并排序
def merge(L1, L2):
    '''Merge sorted lists L1 and L2 and return the result.'''
    newL = []
    i1 = 0
    i2 = 0

    # For each pair of items L1[1], L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 +=1
        else:
            newL.append(L2[i2])
            i2 += 1

    newL.extend(L1[i1:])
    newL.extend(L2[i2:])

    return newL
if __name__ == '__main__':
    lista = [10, 5, 3, 4, 100, 89, 20]
    print( bin_sort(lista))

    print(merge([1,3,5,7], [2,7,9,10,22,33]))

