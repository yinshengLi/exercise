#__author:iruyi
#date:2018/11/2

#linear search one 基本线性搜索
def linear_search(v, L):
    '''Return the index of the first occurrence of v in list L, or return len(L) if v is not in L.'''
    i = 0
    #Keep going until we reach the end of L or until we find v.
    length = len(L)
    while i != length and L[i] != v:
        i  = i + 1

    return i

#linear search two for循环型线性搜索
def linear_search2(v, L):
    '''Return the index of the first occurrence of v in list L, or return len(L) if v is not in L.'''
    i = 0
    for value in L:
        if value == v:
            return i
        i += 1
    return len(L)

#linear search three 哨兵搜索
def linear_search3(v, L):
    '''Return the index of the first occurrence of v in list L, or return len(L) if v is not in L.'''
    i = 0
    # add the sentinel
    L.append(v)
    # Keep going until we  until we find v.
    while L[i] != v:
        i += 1
    L.pop()
    return i

if __name__ == '__main__':
    lista = [2, 5, 7, 9, 10]
    print('first:', linear_search(5, lista))
    print('second:', linear_search2(3, lista))
    print('third:', linear_search3(7, lista))