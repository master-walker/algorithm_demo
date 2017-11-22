#!/usr/bin/env python
#coding=utf-8

'''
test knowledge
'''


'''
给定一个全是整数的一个数组，找出重复次数最多的前N个元素，并且按次数降序排列，返回一个数组

'''


arr = [1,2,3,2,1,3,2,1,5,6,7,7,2]
arr2 = [3,2,56,3,2,3,3,1,2,6,7,8,8,8,66,6,5]
def find_repeat_element(arr):
    repeat_dict = {}
    for ele in arr:
        # 用array.count(ele)计算元素出现的次数
        repeat_count = arr.count(ele)
        if repeat_count > 1:
            # 把重复的元素做key,重复次数作为value，存为字典
            repeat_dict[ele] = repeat_count
    sort_dict = sorted(repeat_dict.iteritems(),key=lambda d:d[1],reverse=True)
    sort_arr = [i[0] for i in sort_dict]
    print sort_arr
    print sort_dict
    return sort_arr


find_repeat_element(arr)
find_repeat_element(arr2)