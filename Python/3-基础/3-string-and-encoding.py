# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字符串和编码
# 第一行注释：告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释：告诉Python解释器，按照UTF-8编码读取源代码，否则，在源代码中写的中文输出可能会有乱码
# 申明了UTF-8编码并不意味着.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 with BOM编码


# 字符编码
# ASCII编码：大小写英文字母、数字、一些符号；1个字节
# GB2312编码：汉字
# Unicode编码：把所有语言都统一到一套编码；通常是2个字节
# UTF-8编码：可变长编码；把一个Unicode字符根据不同的数字大小编码成1-6个字节
# 常用的英文字母被编码成1个字节；汉字通常是3个字节

# Python的字符串
# 在Python 3版本中，字符串是以Unicode编码的，也就是，Python的字符支持多语言
print('包含中文的str')
# 对于单个字符的编码，Python提供了
# ord()函数：获取字符的整数表示
print('ord()', ord('A'))
# 65
# chr()函数：把编码转换为对应的字符
print('chr()', chr(66))
# 'B'
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
# 'abc'：是str
# b'abc'：每个字符都只占一个字节
# encode()函数：以Unicode表示的str可以编码为指定的bytes
# print('ABC'.encode('ascii'))
# 如果str中包含无法编码的字节，encode()方法会报错
# 'ABC'
# decode()函数：把bytes变为str
# 如果bytes中包含无法解码的字节，decode()方法会报错
# 如果bytes中只有一小部分无效的字节，可以传入errors = 'ignore'忽略错误的字节
# print(b'ABC'.decode('ascii'))
# 'ABC'
# len()函数：计算字符数或字节数
print('字符数', len('ABC'))
# 3
print('字符数', len('中文'))
# 6 一个中文字符经过UTF-8编码通常会占用3个字节，而1个英文字符只占用1个字节

# 格式化
# 1---使用占位符
# 占位符 %d：表示用整数替换；指定是否补0
print('%02d-%3d' % (3, 1))
# 03-  1
# 占位符 %f：表示用浮点数替换；可以指定小数的位数
print('%.2f' % 3.1415926)
# 3.14
# 占位符 %s：表示用字符串替换
# 如果不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('age = %s, gender = %s' % (18, True))
# age = 18, gender = True
# 占位符 %x：表示用十六进制整数替换
# 转义：用%%来表示一个%
# 2---使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}......
print('hello, {0}! my_name is {1}'.format('damon', 'stefan'))
# hello, damon! my_name is stefan
