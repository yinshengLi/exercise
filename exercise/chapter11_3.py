#__author:iruyi
#date:2018/11/2
# 排序

def find_largest(N, L):
    '''Return the N largest values in L in order from smallest to largest.'''
    copy = L[:]
    copy.sort()
    copy.reverse()
    return copy[:N]

if __name__ == '__main__':
    lista = [4, 6, 9, 10, 2, 7]
    print(find_largest(3, lista))