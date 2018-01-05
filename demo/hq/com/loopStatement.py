#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 循环语句

# while循环（while … else 在循环条件为 false 时执行 else 语句块：）
import time # alt + enter 自动导入

count = 0
while(count<10):
    print count;
    count+=1;
else:
    print "已经到10了，结束了"
print "over...."

# for循环
for item in "fuck":
    print item;

list = ["sdf","dw234","sdfsdf"]
for item in list:
    print item;

print len(list) # 获取list大小

# 通过序列索引迭代 类似java中的for(i=0;i<size;i++)
for index in range(len(list)):
    print list[index]

# 内置 enumerate 函数进行遍历
for index,item in enumerate(list):
    print index,item

# 类型强转
rows = int(1);
print rows
ff = str(1);
print ff

# 日期类型
print time.time()
print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# import calendar
# cal = calendar.month(2017,1);
# print cal