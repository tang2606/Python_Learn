# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 21:46 
# @Author :  wadedong
# @Site :  
# @File : config.py 
# @Software: PyCharm
from configparser import ConfigParser

import pymysql
class Config():

    def __init__(self):

        self.cfg = ConfigParser()
        self.cfg.read('env.ini')


    def selcet_db(self):




        print(self.cfg.sections())
        print(self.cfg.get('databases','port'))
        print(self.cfg.get('databases', 'port1'))






if __name__ == '__main__':
    Config().selcet_db()