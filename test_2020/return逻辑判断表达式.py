# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : return逻辑判断表达式.py
@Time    : test_2020/4/24 5:23 下午
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""
def fun1():
    '''
    动作分解：

    第一步："21" and True  返回结果 True
    第二步：True or 1  返回结果 True
    注意第二步 True or 1 中的 True 是第一步返回的结果并不是表达式中的True
    '''
    return "21" and True or 1  #等价：return (("21" and True) or 1)

def fun2():
    '''
    动作分解：

    第一步："" or False  返回结果 False
    第二步：False and 0  返回结果 False
    注意第二步 False and 0 中的 False 是第一步返回的结果并不是表达式中的 False
    '''
    return "" or False and 0 #等价：return (("" or False) and 0)

def fun3():
    '''
    动作分解：

    第一步：0 or True  返回结果 True
    第二步：True and False  返回结果 False
    第三步：False or 54  返回结果 54
    第四步：54 and 0  返回结果 0
    注意:上一步的结果作为下一步的开始
    '''
    return 0 or True and False or 54 and 0 #等价：return ((((0 or True) and False) or 54) and 0)

def fun4():
    '''
    动作分解：

    第一步：0 and True and False  返回结果 0
    第二步：0 or 54  返回结果 54
    第三步：54 and 0  返回结果 0
    注意:上一步的结果作为下一步的开始
    '''
    return 0 and True and False or 54 and 0 #等价：return (((0 and True and False) or 54) and 0)

print(fun1())
print(fun2())
print(fun3())
print(fun4())