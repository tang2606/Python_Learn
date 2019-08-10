# -*- coding: utf-8 -*-

"""
    @ Topic:
    @ Author:  wadedong
    @ Company:
    @ CreateTime:  2018-04-17 11:49
    @ Usage:
"""


import requests
import os
from tkinter.filedialog import askdirectory
from Config.Bus_base import BusBase
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox




class DownlodMM(BusBase):

    def __init__(self):

        self.list = ('jk制服','夏日泳装','女仆','兔女郎','动漫类','萝莉','少女','御姐','巨乳','丰满微胖','黑丝','肉丝','网丝','吊带袜','腿控','脚控','臀控','旗袍')

        self.taobao_list =  ['胖次猫','七了个三']



    def Down_pic(self):

        if downlod_path.get() == '':
            tk.messagebox.showerror(title='下载错误',message='没有选择下载路径，请先选择下载路径')
        else:
            url = 'https://api.uomg.com/api/rand.img4?sort={}&format=json'.format(tuwan_text_list.get())
            self.request_img(url)

    def Down_taobao(self):

        if downlod_path.get() == '':
            tk.messagebox.showerror(title='下载错误',message='没有选择下载路径，请先选择下载路径')
        else:

            taobao_url = 'https://api.uomg.com/api/rand.img3?sort={}&format=json'.format(taobao_text_list.get())

            i = 0
            while i < 100:
                req = requests.get(taobao_url)

                pic_dl_url = req.json().get('imgurl')

                filename, old_extension = os.path.splitext(pic_dl_url)

                taobao_img_path = downlod_path.get() + '/' + 'taoba买家秀' + str(i+1).zfill(3) + old_extension

                self.save_pic(pic_url=pic_dl_url,save_path=taobao_img_path)

                i += 1



    def request_img(self,url_list):

        res = requests.get(url=url_list)
        dowlod_list = res.json().get('imgurl')
        img_name = res.json().get('title')
        err_code = res.json().get('code')

        if err_code == 1:
            img_path = downlod_path.get() + '/' + img_name
            number = 0

            if os.path.exists(img_path) == True:
                pass
            else:
                os.makedirs(img_path)



            for img_url in dowlod_list:

                save_img_path = img_path + '/' + img_name + str(number) + '.jpg'

                self.save_pic(save_path=save_img_path,pic_url=img_url)

                number += 1

        else:
            # print(self._get_value_new(res.text,'$.msg'))
            print(res.json().get('msg'))


    def save_pic(self,pic_url,save_path):

        pic_res = requests.get(pic_url)

        open(save_path, 'wb').write(pic_res.content)



    def Downlod_Path(self):
        path =askdirectory()
        downlod_path.set(path)


    def test(self):
        print('xiazai:{}'.format(type(downlod_path.get())))



if __name__ == '__main__':
    dl_pic = DownlodMM()
    window = tk.Tk()
    window.title('美女图片下载')
    window.geometry('370x160')
    downlod_path = tk.StringVar()
    tuwandllist = tk.StringVar()
    taobao_list = tk.StringVar()

    dl_path_name = tk.Label(text='下载路径：').place(x=10, y=10)
    dl_path_in = tk.Entry(window,textvariable=downlod_path).place(x=80, y=10)
    dl_path_bt = tk.Button(text='路径选择', command=dl_pic.Downlod_Path).place(x=280, y=10)

    tuwan_text_list = tk.ttk.Combobox(window, textvariable=tuwandllist, width=13)
    tuwan_text_list.place(x=80, y=40)
    tuwan_text_list["value"] = dl_pic.list
    tuwan_text_list.current(1)
    tuwan_text_list_bt = tk.Button(text='兔玩图片下载', command=dl_pic.Down_pic).place(x=250, y=40)

    taobao_text_list = tk.ttk.Combobox(window, textvariable=taobao_list, width=13)
    taobao_text_list.place(x=80, y=80)
    taobao_text_list["value"] = dl_pic.taobao_list
    taobao_text_list.current(0)
    dl_taobao_bt = tk.Button(text='淘宝买家秀下载', command=dl_pic.Down_taobao).place(x=250, y=80)

    # test = tk.Button(text='Test', command=dl_pic.test).pack()

    window.mainloop()
