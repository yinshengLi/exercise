#__author:iruyi
#date:2018/10/11

# bubble sort 气泡排序
def bubble_sort(nums):
    for i in range(len(nums) -1):
        for j in range(len(nums) -i -1):
            if nums[j] < nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums

'''
数组中的数字本是无规律的排放，先找到最小的数字，把他放到第一位，然后找到最大的数字放到最后一位。
然后再找到第二小的数字放到第二位，再找到第二大的数字放到倒数第二位。以此类推，直到完成排序。
'''
def cocktailSort(nums):
    size = len(nums)
    for i in range(size//2):
        for j in range(i, size-i-1):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        #将最大值排到队头  (size-i-2 因为上面执行就会排好一个最小的，所以就要少排一个)
        for j in range(size-i-2, i, -1):
            if nums[j] > nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

# direct insert sort
def directInsertSort(nums,n):
    for i in range(1, n):
        temp = nums[i]
        j = i -1
        while j > -1 and temp < nums[j]:
            nums[j+1] = nums[j]
            j = j-1
        nums[j+1] = temp

def insertSort(nums):
    size = len(nums)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]


lista = [10, 40, 3, 5, 9, 80, 100]
print('origin:', lista)

# print('bubble_sort:',bubble_sort(lista))
# print('cocktail_sort:', cocktailSort(lista))

# directInsertSort(lista,len(lista))
# print('directInsertSort',lista)
# insertSort(lista)
# print('insertSort', lista)
