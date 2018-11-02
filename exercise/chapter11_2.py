#__author:iruyi
#date:2018/11/2

# 二分法

def binary_search(v, L):
    ''' Return the index of the leftmost occurrence of v in list L, or -1
    if v is not in L.'''

    # Mark the left and right indices of the unknown sectic
    i = 0
    j = len(L)-1

    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v:
            i = m + 1
        else:
            j = m -1

    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1

if __name__ == '__main__':
    lista = [1, 4, 7, 10, 21, 45, 78, 90, 99]
    # print(binary_search(1, lista))
    print(binary_search(21, lista))
    # print(binary_search(99, lista))