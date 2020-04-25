# -*- coding: utf-8 -*- 
# @Time : 2019/8/25 23:46 
# @Author :  wadedong
# @Site :  
# @File : test.py 
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests


r = requests.get('http://tieba.baidu.com/p/2460150866')
r.encoding = r.apparent_encoding


soup = BeautifulSoup(r.text,'html.parser')


print(soup.find_all('img'))
img_list = soup.find_all('img',{'class':'BDE_Image'})

for img_url in img_list:
    img= img_url.get("src")
    print(img)

