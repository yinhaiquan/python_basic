#!/usr/bin/python
# -*- coding: UTF-8 -*-
# gui编程 类似java awt/swing

import Tkinter
top = Tkinter.Tk()
# 进入消息循环
li = ["->","--","-!-","><","~|||"]
movie = [1,2,3,4,5]

listb = Tkinter.Listbox(top)
listc = Tkinter.Listbox(top)
for item in li:
    listb.insert(0,item);
for item in movie:
    listc.insert(0,item);
listb.pack();
listc.pack();
top.mainloop()

import json
json = json.dumps([{"sdf":123},{"sdf":456}]);
print json