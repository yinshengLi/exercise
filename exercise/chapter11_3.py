#__author:iruyi
#date:2018/11/2
# 排序
# 找到最大的N个值
def find_largest(N, L):
    '''Return the N largest values in L in order from smallest to largest.'''
    copy = L[:]
    copy.sort()
    copy.reverse()
    return copy[:N]


# 选择排序
def selection_sort(L):
    '''Recorder the items in L from smallest to largest.'''
    i = 0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

def find_min(L, b):
    '''Returen the index of the smallest value in L[b:].'''
    smallest = b # The index of the smallest so far.
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            # We found a smaller item at L[i]
            smallest = i
        i = i + 1
    return smallest

# 插入排序
def insertion_sort(L):
    '''Reorder the values in L from smallest to largest.'''
    i = 0
    while i != len(L):
        insert(L, i)
        i = i + 1

def insert(L, b):
    ''' Insert L[b] where it belongs in L[0:b+1];
    L[0:b-1] must already be sorted.'''

    #Find where to insert L[b] by searching backwards from L[b] for a smaller item.
    i = b
    while i != 0 and L[i-1] >= L[b]:
        i = i-1
    # Move L[b] to index i, shifting the following values to the right.
    value = L[b]
    del L[b]
    L.insert(i, value)


if __name__ == '__main__':
    lista = [4, 6, 9, 10, 2, 7]
    print(find_largest(3, lista))
    print("orgin:", lista)
    # selection_sort(lista)
    insertion_sort(lista)
    print("sorted:", lista)