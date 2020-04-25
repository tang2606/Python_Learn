# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : 不定长参数.py
@Time    : test_2020/4/25 14:49
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""
import time

#for 循环生成列表
list1 = []
start_time1 = time.time()
for i in range(0,10000000):
    list1.append(i)
end_time1 = time.time()
print('for循环生成需要时间：{}'.format(start_time1-end_time1))


# 列表推导式生成列表

start_time2 = time.time()
list2 = [i for i in range(0,10000000)]
end_time2 = time.time()

print('推导式 生成需要时间：{}'.format(start_time2-end_time2))
