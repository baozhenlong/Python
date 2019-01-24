# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用dict和set

# dict
# Python内置字典；使用键-值(key-value)存储，具有极快的查找速度
d = {
    'damon': 20,
    'stefan': 19
}
print(d['damon'])
# 20
d['Elena'] = 18
print(d['Elena'])
# 18
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Elena'] = 19
print(d['Elena'])
# 19
# 访问一个不存在的key，dict就会报错
# 通过in判断key是否存在
print('damon' in d)
# True
# 通过dict提供的get()方法，如果key不存在，可以返回None，或自己指定的value
print(d.get('x'))
# None
print(d.get('x'), -1)
# (None, -1)
# pop(key)：删除一个key，对应的value也会从dict中删除
print(d)
# {'damon': 20, 'Elena': 19, 'stefan': 19}
d.pop('Elena')
print(d)
# {'damon': 20, 'stefan': 19}
# dict内部存放的顺序和key放入的顺序是没有关系的
# 和list比较
# dict的特点：
# 查找和插入的速度极快，不会随着key的增加而变慢
# 需要占用大量的内存，内存浪费多
# list的特点
# 查找和插入的时间随着元素的增加而增加
# 占用空间小，浪费内存很少
# 所以，dict是用空间来换取时间的一种方法
# dict可以用在需要高速查找的很多地方
# 注意：dict的key必须是不可变对象
# 这是因为dict根据key来计算value的存储位置(哈希算法)，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key；而list是可变的，就不能作为key

# set
# 和dict类似，也是一组key的集合(不是有序的)，但不存储value
# 由于key不能重复，所以，在set中，没有重复的key
# 创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)
# set([1, 2, 3])
# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)
# set([1, 2, 3])
# add（key)：添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
# set([1, 2, 3, 4])
s.add(4)
print(s)
# set([1, 2, 3, 4])
# remove(key)：删除元素
s.remove(4)
print(s)
# set([1, 2, 3])
# set可以看成数学意义上的无序和无重复元素的集合
# 因此，2个set可以做数学意义上的交集、并集等操作
s_1 = set([1, 2, 3])
s_2 = set([2, 3, 4])
print(s_1 & s_2)
# set([2, 3])
print(s_1 | s_2)
# set([1, 2, 3, 4])
# set和dict的唯一区别：仅在于没有存储对应的value
# set同样不可放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部"不会有重复元素"

# 不可变对象
a = 'abc'
# a本身是一个变量，它指向的对象的内容才是'abc'
b = a.replace('a', 'A')
print(b)
# Abc
# replace方法：返回一个新字符串
print(a)
# abc
