#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 数据类型
"""
在内存中存储的数据可以有多种类型。
例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
Python 定义了一些标准类型，用于存储各种类型的数据。
Python有五个标准的数据类型：
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
"""

int = 100 # 赋值整型变量
float = 100.1231 # 浮点型
name = 'fk' # 字符串
print int , float,name

# 多个变量赋值
a = b = c = 1
print a;print b;print c;
a,b,c=1,2,3
print a;print b;print c;
# del a,b,c; #del语句删除一些对象的引用
print a

# 字符串
str = 'what is the fuck about python?';
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串
print str.__len__() # 输出字符串长度
print str.split(" ");

# list列表（类似java的list和数组）
list = ['sdf','234','s234','中国'];
list2 = ['sdf','234'];
print list.__len__()
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print list2 * 2          # 输出列表两次
print list + list2       # 打印组合的列表

# tuple 元组(只读)
"""
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
"""

tuple = ('123','231',123,'sj','呵呵');
tuple2 = ('123',123);
print tuple
print tuple[0]
print tuple[2:3]
print tuple[2:]
print tuple * 2
print tuple + tuple2
print tuple[tuple.__len__()-1]

# dictionary 字典(类似java集合set)
"""
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
"""
dict = {}
dict['fuck'] = "fk"
dict[0]=123
dict2 = {"fuck":"fk too","sdf":"sdf"}

print dict['fuck']  # 输出键为'fuck' 的值
print dict[0]       # 输出键为 0 的值
print dict          # 输出完整的字典
print dict2.keys()  # 输出所有键
print dict2.values()# 输出所有值

# 数据类型转换
