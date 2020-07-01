# !usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : m163_headlines.py
@Time    : 2020/7/1 5:18 下午
@Author  : wade.dong
@Email   : wadedong2606@gmail.com
@Software: PyCharm
"""

import requests


class Get_163_HeadLines():

	def __init__(self):
		pass
	def get_url(self,Url):
		pass


	def main(self):
		url = "http://c.m.163.com/nc/article/headline/T1348647853363/0-100.html"
		res = requests.get(url=url)

		headlinesdata = res.json()

		get_key = list(headlinesdata.keys())[0]

		data_list = headlinesdata.get(get_key)


		i = 0
		for news in data_list:
			i += 1
			print(f"{i}、标题：{news.get('title')} - {news.get('ptime')}\n简要：{news.get('digest')} \n新闻星期三地址：{news.get('url')}")









if __name__ == '__main__':
	Get_163_HeadLines().main()