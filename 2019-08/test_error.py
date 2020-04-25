# -*- coding: utf-8 -*- 
# @Time : 2019/8/25 18:32 
# @Author :  wadedong
# @Site :  
# @File : test_error.py 
# @Software: PyCharm

class wadeError(Exception):

    def __init__(self,msg):
        self.err_msg = msg



a = 1


try:
    assert a == 2, '123'

    raise wadeError('这他妈就不合理')

except wadeError as e:
    print(e)
except AssertionError as e :
    print(e)