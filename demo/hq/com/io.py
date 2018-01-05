#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 文件io

# 控制台输入
# str = raw_input("请输入:") # 输入的参数是数据
# print "输入的内容："+str

# str = input("请输入:") # 参数是表达式
# print "输入的内容：",str

# 打开文件 (若文件不存在，自动创建文件)
file = open("function.py","r");
print "文件名：",file.name
print "是否已关闭：",file.closed
print "访问模式：",file.mode
file.close()
print "是否已关闭：",file.closed

# 打开文件
file = open("test.txt","wb")
print file.name
# 写数据
file.write("skldjflksdjflksjdfkljskdf\n")
# 关闭文件
file.close()

# 打开文件
file = open("test.txt","r")
# 读数据
str = file.read(5)
# print str
# print file.read()
for line in file.readlines():
    print line
# 关闭文件
file.close()

# try 异常捕捉
"""
以下为简单的try....except...else的语法：
    try:
    <语句>        #运行别的代码
    except <名字>：
    <语句>        #如果在try部份引发了'name'异常
    except <名字>，<数据>:
    <语句>        #如果引发了'name'异常，获得附加的数据
    else:
    <语句>        #如果没有异常发生
    
    raise 抛出异常 类似java throw
"""
try:
    print 1/0;
except Exception as e:
    print e.message
else:
    print 123
