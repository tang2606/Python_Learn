# -*- coding: utf-8 -*- 
# @Time : 2019/8/25 23:29 
# @Author :  wadedong
# @Site :  
# @File : test_init.py 
# @Software: PyCharm
from Games.test import config

class test_(config):
    def __init__(self):
        super(config,self).__init__()
        self.twd = 'tangweidong'
        self.wade = 'wadedong'
        self.name = config().names
        self.sex = config().sex

    def check(self):

        return self.name,self.sex,self.twd



print(test_().check())