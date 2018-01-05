#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 模块 类似java 引入其他的类
import sys

import os

import function

print "---------分割线--------"
print function.getName("sdf",123)


from function import showName
showName("呵呵哒")

# sys os 模块
print sys.path # 是一个list,指明所有查找module，package的路径.
print sys.platform # 得到运行的操作系统环境
print sys.modules # 是一个dictionary，表示系统中所有可用的module

print os.environ #  一个dictionary 包含环境变量的映射关系
print os.environ['JAVA_HOME'] #可以得到环境变量HOME的值
print os.getcwd() # 得到当前目录