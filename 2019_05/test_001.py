# -*- coding: utf-8 -*- 
# @Time : 2019/11/10 17:35 
# @Author :  wadedong
# @Site :  
# @File : test_001.py 
# @Software: PyCharm

import os
class Test():
    def t01(self,path=None):
        if path:
            file_list = os.walk(path)
            # for files in file_list:
            #     print(files)
            print(file_list.__next__())
        else:
            print(2)


if __name__ == "__main__":
    Test().t01('F:\MyCode\Python_Learn')