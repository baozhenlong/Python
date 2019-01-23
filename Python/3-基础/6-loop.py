# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环
# 1---for...in循环；依次把list或tuple中的每个元素迭代出来
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
names = ['damon', 'stefan', 'Elena']
for name in names:
    print(name)
# damon
# stefan
# Elena
sum = 0
# range(max_num)：可以生成一个整数序列；生成的序列是从0开始，小于max_num的整数
num_list = list(range(5))
print(range(5))
# [0, 1, 2, 3, 4]
print(num_list)
# [0, 1, 2, 3, 4]
for num in num_list:
    sum = sum + num
print(sum)
# 10 1+2+3+4
# 2---while循环
# 只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 3
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
# 6 1+2+3

# break
# 退出循环
n = 1
while n < 10:
    if(n > 3):
        break
    n = n + 1
print(n)
# 4

# continue
# 结束本轮循环，直接开始下一轮循环
n = 0
while n < 4:
    n = n + 1
    if(n % 2 == 0):
        continue
    print(n)
# 1
# 3
