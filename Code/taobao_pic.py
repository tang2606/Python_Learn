# -*- coding: utf-8 -*-

"""
    @ Topic:
    @ Author:  wadedong
    @ Company:
    @ CreateTime:  2019-06-17 16:31
    @ Usage:
"""




import requests
import random
import os


class taobao():

    def downlod(self):

        case = ['胖次猫','七了个三']

        # url = 'https://api.uomg.com/api/rand.img3?sort={}&format=json'.format(random.choice(case))
        url = 'https://api.uomg.com/api/rand.img3?sort={}&format=json'.format('胖次猫')

        req = requests.get(url)

        print(req.json().get('imgurl'))

    def test01(self):

        filename, old_extension = os.path.splitext('https://gw3.alicdn.com/tfscom/tuitui/TB2Ef5WtCJjpuFjy0FdXXXmoFXa_!!0-rate.jpg')

        # print(filename,'12e',old_extension)

        a = {'code': 1, 'imgurl': 'https://gw2.alicdn.com/tfscom/tuitui/O1CN01wEhAg11EQxusYIR9t_!!0-rate.jpg'}

        print(a.get('imgurl'))


    def test02(self):
        a = {'err_code': 0, 'err_msg': '操作成功', 'data': {'data': {'accept_count': 0, 'accept_total': 0, 'repay_count': 0, 'repay_total': 0, 'call_amount': 0, 'talk_time': 0, 'action_amount': 0, 'twd': {'wade': 1, 'dong': 'tangweidong'}}, 'statics_date': '2019-06-17 15:12', 'type': '1'}}
        b = a.get('data').get('data').get('twd').get('dong')
        # c = b.get('accept_count')
        print(b)

    def test03(self):

        for n in (1,2,3,4):
            i = 0
            while i < 10:
                print(n,i)
                i += 1


if __name__ == '__main__':
    run = taobao()

    run.test03()