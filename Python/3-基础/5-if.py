# /!usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断
age = 20
if age >= 18:
    print('adult, your age is', age)
elif age >= 6:
    # elif是else if的缩写
    print('teenager, your age is', age)
else:
    print('kid, your age is', age)
# ('adult, your age is', 20)
# 简写if判断条件
x = [1]
# x = (1, )
if x:
    # 只要x是非0数值、非空字符串、非空list等，就判断为True，否则为False
    print(True)

# input
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转成整数
# int()：把字符串转为整数；如果字符串并不是合法的数字时就会报错
str = input('num：')
num = int(str)
if num < 10:
    print('个位数 num =', num)
else:
    print('不是个位数 num =', num)