#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 面向对象
'''
_表示私有属性 类似java protected
__表示私有属性 类似java private
__init__（） 表示构造函数

注意：
    使用类继承时，若需要继承父类构造函数，则父类必须是新类

    新类和金典类区别：http://blog.csdn.net/gui694278452/article/details/49308605
    新类     继承了其他类
    金典类   未继承其他类，普通类

    故，再编写类时务必继承object类
'''

'定义一个普通类'


class DemoClass(object):
    __count__ = 1;
    _name = '123';
    __name2 = '234';

    def __init__(self, count, name):
        print '调用父类构造函数'
        self.__count__ = count;
        self._name = name;

    def getCount(self):
        print self._getName()
        return self.__count__;

    def _getName(self):
        return self._name;

    def __getName2(self):
        return self.__name2


# 实例化类
dc = DemoClass("fuck", "fuck")
print dc.__count__
print dc.getCount()

print '---------------子类----------------'

# 调用父类方式一
class Child(DemoClass):
    def __init__(self):
        DemoClass.__init__(self,"sdf","sdf")
        print '调用子类构造函数'

    _fuck = 123;

c = Child();
print c.getCount()

# 调用父类方式二
class Child2(DemoClass):
    def __init__(self):
        super(Child2,self).__init__("sdf","sdf")
        print '调用子类构造函数'

    _fuck = 123;

c = Child2();
print c.getCount()