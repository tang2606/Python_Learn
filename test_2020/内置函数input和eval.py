# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : 内置函数input和eval.py
@Time    : test_2020/4/24 5:49 下午
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""

while True:
    '''
    replace("?","!") 将字符串中英文状态下的问号 ？替换为 感叹号 ！ 
    replace("？","!")将字符串中中文状态下的问号 ？替换为 感叹号 ！
    replace("吗","") 将字符串中的中文 "吗" 替换为 ""
    '''
    input_ = input("请输入：")
    if input_ == 'exit' or input_ == '':
        break

    else:
        print('电脑：',input_.replace("?","!").replace("？","!").replace("吗",""))


while True:

    result  = lambda input_=input("请输入表达式："): False if input_ == 'exit' or input_ == '' else eval(input_)
    if result() == False:
        exit(1)
    print("结果：", result())

