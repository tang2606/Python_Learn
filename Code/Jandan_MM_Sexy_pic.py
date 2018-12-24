# -*- coding: utf-8 -*-

"""
    @ Topic:
    @ Author:  weidong.tang
    @ Company:
    @ CreateTime:  2018-04-17 11:49
    @ Usage:
"""
import datetime
import os
from tkinter.filedialog import askdirectory

import requests
from tkinter import *           # 导入 Tkinter 库
from tkinter import messagebox




def Down_loand_pics(url, ooscore):

    headers = {'User-Agent': 'Jandan Android App V5.1.0.0'}
    req = requests.get(url=url, params=headers)
    JD_comments = req.json()['comments']

    for i in JD_comments:
        pics_list_name = i['comment_author']
        pics_list_number = i['vote_positive']
        pics_list_pic = i['pics'][0]
        vote_positive =int(i['vote_positive'])
        name = pics_list_name + pics_list_number + pics_list_pic[-4:]
        if vote_positive > ooscore:
            ir = requests.get(pics_list_pic)
            save_jpg = open('/Users/wade/Downloads/temp/xxoo/' + name, 'wb').write(ir.content)
            print(save_jpg)
            print('%s Save OK !' % (name))
        else:
            print('%s 评分小于%d跳过下载，实际评分：[%d] '%(pics_list_name, ooscore, vote_positive))


def donwload():
    a = 0
    url_temp = 'http://i.jandan.net/?oxwlxojflwblxbsapi=jandan.get_ooxx_comments&page='
    headers = {'User-Agent': 'Jandan Android App V5.1.0.0'}
    insetkey = int(startpage.get())
    oo_score = int(ooscore.get())
    donwlist = Listbox(root)
    errimg_msg = Listbox(root)
    today = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    path = '/Users/wade/Downloads/temp/xxoo' + str(today)
    os.makedirs(path)

    while a <= insetkey:
        url = url_temp + str(a)
        req = requests.get(url=url, params=headers)
        JD_comments = req.json()['comments']
        for i in JD_comments:
            pics_list_name = i['comment_author']
            pics_list_number = i['vote_positive']
            pics_list_pic = i['pics'][0]
            vote_positive = int(i['vote_positive'])
            name = pics_list_name + pics_list_number + pics_list_pic[-4:]

            if vote_positive > oo_score:
                ir = requests.get(pics_list_pic)
                save_jpg = open(path + '/' + name, 'wb').write(ir.content)
                donwlist.insert(0, name)
                print(name)

            else:
                errormsg = str(pics_list_name) + pics_list_pic[-4:] + '评分小于' + str(oo_score) + '跳过下载，实际评分：' + str(vote_positive)
                print(errormsg)
                errimg_msg.insert(0, errormsg)
        a = a + 1
    donwlist.pack(side=LEFT)
    errimg_msg.pack(side=RIGHT)
    root.mainloop()



root = Tk()#创建窗口对象的背景色
root.title('煎蛋网妹子图批量下载器')
root.iconbitmap('ic.ico')
button_frame = Frame(root)
button_frame.pack(side=RIGHT)

startpage = Entry(button_frame)
startpage.grid(row=0, column=1, padx=3, pady=3)
startpage_label = Label(button_frame, text='请输入需要下载的页码')
startpage_label.grid(row=0, column=0, padx=3, pady=3)
startpage.insert(0, "50")
ooscore = Entry(button_frame)
ooscore.grid(row=1, column=1, padx=3, pady=3)
ooscore_label = Label(button_frame, text='请输入需要过滤的分值')
ooscore_label.grid(row=1, column=0, padx=3, pady=3)
ooscore.insert(0, "80")

DownloadImg = Button(button_frame, text='下载', command=donwload, width=16, height=1)
DownloadImg.grid(row=3, column=1, padx=3, pady=3)

mainloop()
