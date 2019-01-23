# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# list：列表
# 列表：Python内置的一种数据类型
# list是一种有序的集合，可以随时添加和删除其中的元素
# 1---定义
classmates = ['damon', 'stefan']
print(classmates)
# ['damon', 'stefan']
# 2---长度
# len()：可以获得list元素的个数
print(len(classmates))
# 2
print(len([]))
# 0
# 3---访问
# 用索引来访问list中每一个位置的元素，索引从0开始
print(classmates[0])
# damon
# 当索引超出了范围时，Python会报一个IndexError错误
# print(classmates[11])
# IndexError: list index out of range
# 所以要确保不要越界，记得最后一个元素的索引是len(classmates) - 1
# 获取最后一个元素：除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
# stefan
# 传入-2可以获取倒数第二个；也会越界
print(classmates[-2])
# damon
# 4---添加元素到末尾
classmates.append('Elena')
print(classmates)
# ['damon', 'stefan', 'Elena']
# 5---删除末尾元素
classmates.pop()
print(classmates)
# ['damon', 'stefan']
# 5---插入元素到指定位置
classmates.insert(1, 'Elena')
print(classmates)
# ['damon', 'Elena', 'stefan']
# 6---删除指定位置的元素
classmates.pop(1)
print(classmates)
# ['damon', 'stefan']
# 7---替换元素
classmates[1] = 'Elena'
print(classmates)
# ['damon', 'Elena']
# list里面的元素的数据类型可以不同，元素也可以是另一个list
s = [1, [2, 3], 4]
print(s[1][1])
# 3

# tuple：元组
# 与list非常类似，但是tuple一旦初始化就不能修改
# 1---定义时必须初始化
t = (1, 2)
print(t)
# (1, 2)
print((1))
# 1
# Python规定，这种情况下，按小括号进行计算
# 只有一个元素的tuple定义时必须加一个逗号来消除歧义
print((1,))
# (1,)
t = ('a', [1, 2, 3])
print(t)
('a', [1, 2, 3])
t[1].append(4)
print(t)
('a', [1, 2, 3, 4])
# 不能修改，指的是指向永远不变
