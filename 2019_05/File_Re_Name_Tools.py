# -*- coding: utf-8 -*-

"""
    @ Topic:
    @ Author:  wadedong
    @ Company:
    @ CreateTime:  2019-06-04 17:43
    @ Usage:
"""

import os
import time
import tkinter.filedialog
import requests




class file_tools():

    def Renames(self,inset_name):
        now_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        os_path = tkinter.filedialog.askdirectory()
        file_names = os.listdir(os_path)
        num = len(str(len(file_names)))
        i = 1
        print(file_names)
        for file_name_temp in file_names:
            filename, old_extension = os.path.splitext(file_name_temp)
            new_name = '{}/{}_{}_{}_{}{}'.format(os_path, inset_name, filename, now_day, str(i).zfill(num), old_extension)
            os.rename(os_path + '/' + file_name_temp, new_name)
            i +=1

        print('Done!')

    def DelFile(self):
        os_path = tkinter.filedialog.askdirectory()
        for path, dirs, files in os.walk(os_path):
            for fname in files:
                file_size = os.path.getsize(os.path.join(path, fname))

                if file_size:
                    pass
                else:
                    os.remove(os.path.join(path, fname))
                    print('Remove File Done ！ {} Size:{}'.format(fname, file_size))

    def file_(self):
        pass


if __name__ == '__main__':
    a, b = True, False

    aaa = a if a == 0 else b

    print(aaa)
