#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 基础语法

"""
#!/usr/bin/python : 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器；
#!/usr/bin/env python(推荐）: 这种用法是为了防止操作系统用户没有将 python 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。
#!/usr/bin/python 相当于写死了python路径;
#!/usr/bin/env python 会去环境设置寻找 python 目录,推荐这种写法
"""


# Python注释
'''
中文注释方法
Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
注意：#coding=utf-8 的 = 号两边不要空格。
'''
"""
中文注释方法
Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
注意：#coding=utf-8 的 = 号两边不要空格。
"""
# 中文输出
print "呵呵";

# 条件语句
if True:
    print "true"
    print "第二个true"
elif True:
    print "巴拉巴拉"
else:
    print "false"


# 多行语句
item1 = 'fuck';item2='123';item3="呵呵";
total = item1+\
        item2+\
        item3;
print total

# 字符串 Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
word = 'word'
sentence = "balbalabala"
paragraph = """what 还可以这样。"""
print paragraph;

# 控制台输入数据
# print raw_input("\n\npress the enter key to exit.")

import sys;
sys.stdout.write("123\n")

# print 输出 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号
print 123,343,'sdfsdf'