# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 0:00 
# @Author :  wadedong
# @Site :  
# @File : test02.py 
# @Software: PyCharm

import pymysql

def wade():

    conn = pymysql.connect(host='127.0.0.1',
                           user='wade_rw',
                           password='wade_rw',
                           database='twd',
                           charset='utf8',
                           cursorclass =pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql ="select * from twd.mydata;"
    # sql = "desc twd.mydata"
    cursor.execute(sql)
    data_all =cursor.fetchall()


    print(data_all)
    # for a in row:
    #     print(a)
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()

wade()