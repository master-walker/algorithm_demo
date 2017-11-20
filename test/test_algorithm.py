#!/usr/bin/env python
#coding=utf-8

'''

algorithm test demo
'''

'''
鸡兔同笼问题
鸡兔数量一共m,脚的数量为n
鸡兔同时收起两只脚，剩余脚的一半就是兔的数量
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
二分法查找
'''

def binary_search(array, num):
    if not isinstance(array,list):
        print "参数传值异常"
        return False
    else:
        array.sort()
        low = 0
        hight = len(array)-1
        while(low < hight):
            mid = (low + hight) / 2
            if array[mid] < num:
                low = mid + 1
            elif array[mid] > num:
                hight = mid - 1
            else:
                return array[mid],mid
        return -1

# arr = [1,5,3,9,6,6,7]
# num,index = binary_search(arr,7)
# print num,index

'''
冒泡排序
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

arr = [1,5,3,9,6,6,7]
bubble_sort(arr)
