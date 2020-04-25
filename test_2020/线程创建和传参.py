# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : 线程创建和传参.py
@Time    : 2020/4/24 7:04 下午
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""

import threading,random,time
import string

def list1():
    for i in range(0,20):

        print(i, '\n')


def list2():
    for i in string.ascii_letters:

        print(i, '\n')



t1 = threading.Thread(target=list1)
t2 = threading.Thread(target=list2)

t1.start()
t2.start()




