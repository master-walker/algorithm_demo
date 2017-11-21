#!/usr/bin/env python
#coding=utf-8

'''

algorithm test demo
'''

'''
鸡兔同笼问题
鸡兔数量一共m,脚的数量为n
鸡兔同时收起两只脚,收起的数量为2m，剩余脚n-2m的一半就是兔的数量

'''


def get_num(jitu_amount, leg_amount):
    tu_amount = (leg_amount - jitu_amount*2)/2
    print tu_amount
    if int(tu_amount) == tu_amount:
        return (jitu_amount-tu_amount, tu_amount)
    else:
        return -1

# arr= get_num(10,30)
# print arr

'''
二分法查找find_num
查找前提：序列array是有序的
当最小索引low<=最大索引high时，
通过最小索引low和最大索引high，确定中间位置的索引mid
比较array[mid]与find_num的大小
if array[mid]> find_num:
high=mid-1
继续计算新的mid值
else low=mid+1
计算mid的新值
继续循环比较计算，直到不满足low<=high,结束

'''

def binary_search(array, num):
    if not isinstance(array,list):
        print "参数传值异常"
        return False
    else:
        array.sort()
        low = 0
        high = len(array)-1
        while(low <= high):
            mid = (low + high) / 2
            if array[mid] < num:
                low = mid + 1
            elif array[mid] > num:
                high = mid - 1
            else:
                return array[mid]
        return -1

arr = [1,5,3,9,6,6,7]
num = binary_search(arr,0)
print num

'''
冒泡排序
循环交换数组len(array)-1次：
依次从0开始，两两比较，如果前一个位置的数大，就交换位置，
0与1，1与2，... len(arr)-2与len(arr)-1
第一次交换后，最大值移到了最后位置,内层循环减一
第二次交换除最大值以外的值，找到次最大值
1与2，2与3 ... len(arr)-3与len(arr)-2
以此推理，继续循环

'''

def bubble_sort(arr):
    if not isinstance(arr,list):
        print "参数传值异常"
        return False
    else:
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        print arr

# bubble_sort(arr)


'''
插入排序

'''

def insert_sort(arr):
    if not isinstance(arr,list):
        print "参数传值异常"
        return False
    else:
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        print arr
        return arr

insert_sort(arr)




'''
选择排序arr
默认先选择索引0为最大值，max = i
依次与序列的所有值比较，
if arr[oth]>arr[max]:
max = oth
比较一次之后，找到最大值的索引，放到最后

'''


def select_sort(arr):
    # 选择一个最大值排序
    # for i in range(len(arr)-1, 0, -1):
    #     max = i
    #     for j in range(i):
    #         if arr[j] > arr[max]:
    #             max = j
    #     arr[i], arr[max] = arr[max], arr[i]
    # print arr
    # return arr

    # 选择一个最小值排序
    # 选定的最小值的索引必须不断随循环变化
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print arr
    return arr




select_sort(arr)

