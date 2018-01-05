#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 函数

# 无返回值函数 void
def showName(name):
    print name

showName("fuck")

# 有返回值函数 return
def getName(name,age):
    return str(age)+name

print getName("fuck",12)

# 缺省参数 最少得赋值一个参数，且缺省参数必须初始化，否则抛异常
def getParamters(var1,var2=12):
    print var1,var2

getParamters(var1="sdf")
getParamters(var2=123,var1="666")

# 不定长参数
"""
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
和上述2种参数不同，声明时不会命名。基本语法如下:
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
"""

def printInfo(arg0,*args):
    print "输出："
    print arg0
    for item in args:
        print item
    return;

printInfo(10)
printInfo(10,11,12,13)

# 匿名函数
"""
lambda函数的语法只包含一个语句，如下：
      lambda [arg1 [,arg2,.....argn]]:expression
"""
sum = lambda arg0,arg1:arg0+arg1;
print sum(10,10)
print sum(20,20)

# 全局变量
index = 0;
def setIndex():
    global index
    index = 1

def getIndex():
    return index;

setIndex()
print getIndex()