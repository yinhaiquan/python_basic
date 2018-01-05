#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 运算符

"""
    算术运算符
    比较（关系）运算符
    赋值运算符
    逻辑运算符
    位运算符
    成员运算符
    身份运算符
    运算符优先级
"""

# 算术运算符
"""
  运算符	            描述	                                实例
    +	    加 - 两个对象相加	                    a + b 输出结果 30
    -	    减 - 得到负数或是一个数减去另一个数	    a - b 输出结果 -10
    *	    乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
    /	    除 - x除以y	                            b / a 输出结果 2
    %	    取   模 - 返回除法的余数	            b % a 输出结果 0
    **	    幂 - 返回x的y次幂	                    a**b 为10的20次方， 输出结果 100000000000000000000
    //	    取整除 - 返回商的整数部分	            9//2 输出结果 4 , 9.0//2.0 输出结果 4.0

注意：Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。
"""
a = 21;b=10;c=0;
c = a+b;
print c
print a**b
print a//b
print a/b
print a%b

# 逻辑运算符
"""
and or not
"""
print '-----------分割线------------'
print (12 and 2)
print (True and False)
print (True or False)
print not (True)

# 成员运算符
"""
包含了一系列的成员，包括字符串，列表或元组

in	如果在指定的序列中找到值返回 True，否则返回 False。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
"""
a = 12
b = 'asd'
list = ["12",12,"asd"]
tuple = ("12","asd")
print a in list
print a in tuple
print a not in tuple
print a is b
print a is not b
print a == "12"
print "12".__eq__("12")