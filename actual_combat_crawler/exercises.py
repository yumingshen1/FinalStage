# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 14:27
# @Author  : shenyuming
# @FileName: exercises.py
# @Software: PyCharm
'''
编写函数，找到整数数组中的最大值和最小值
'''

def find_max_min(nums):
     if not nums:
         return None,None
     max_val = min_val = nums[0]
     for num in nums:
         if num > max_val:
             max_val = num
         elif num < min_val:
             min_val = num
     return max_val,min_val

'''
一个长方形的长是宽的两倍，如果长方形的周长是24厘米，求长方形的长和宽。
'''
def find_long_wide():
    perimeter = 24
    w = perimeter / 6
    l = 2 * w
    print('长是',l,'厘米')
    print('宽是',w,'厘米')



if __name__ == '__main__':
    print(find_max_min([1,10,3,5,7,2,5]))
    find_long_wide()