# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : 不定长参数.py
@Time    : test_2020/4/24 4:49 下午
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""

def Test(*args,**kwargs):
    print(args)
    print(kwargs)


def Test1(arg,*args):
    print('arg=',arg)
    print('atgs=',args)

def Test2(kwarg,**kwargs):
    print('kwarg=',kwarg)
    print('kwargs=',kwargs)
    print(kwargs.get('c'))
    print(kwargs.values())



Test2('aaaaaaaa',abc=123,c = [11111,22222,3333,44444,55555,66666])
