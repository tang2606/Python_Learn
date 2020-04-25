# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : test_2020-04-24.py
@Time    : test_2020/4/24 4:00 下午
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""

import time
#
# x=15
# print("老司机说：x是偶数1") if x % 2 == 0 else print("老司机说：x是奇数2")


# 字典推导式
cookies = "anonymid=jy0ui55o-u6f6zd; depovince=GW; _r01_=1; JSESSIONID=abcMktGLRGjLtdhBk7OVw; ick_login=a9b557b8-8138-4e9d-8601-de7b2a633f80; _ga=GA1.2.1307141854.1562980962; _gid=GA1.2.201589596.1562980962; _c1=-100; first_login_flag=1; ln_uact=18323008898; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=88f1340c-592c-4dd6-a738-128a76559f45%7Cad33b3c730fcdc8df220648f0893e840%7C1562981108370%7C1%7C1562981106763; jebe_key=88f1340c-592c-4dd6-a738-128a76559f45%7Cad33b3c730fcdc8df220648f0893e840%7C1562981108370%7C1%7C1562981106765; jebecookies=793eb32e-92c6-470d-b9d0-5f924c335d30|||||; _de=E77807CE44886E0134ABF27E72CFD74F; p=a00d65b1f779614cd242dc719e24c73e0; t=292ba8729a4151c1a357e176d8d91bff0; societyguester=292ba8729a4151c1a357e176d8d91bff0; id=969937120; xnsid=1700b2cc; ver=7.0; loginfrom=null; wp_fold=0"

cookies = {cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookies.split("; ")}
print(cookies)


twd = 'a-A,b-B,c-C,d-D'

dict1 = {twd_key.split('-')[0]:twd_key.split('-')[1] for twd_key in twd.split(',')}
print(dict1)


