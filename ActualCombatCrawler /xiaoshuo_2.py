# -*- coding:utf-8 -*-
# @Time : 2024/6/6 21:39
# Auther : shenyuming
# @File : xiaoshuo_2.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup

'''
获取章节信息

'''

if __name__ == '__main__':

    spiderUrl = 'https://www.biqukan.co/book/110254/'
    respones = requests.get(url=spiderUrl)
    respones.encoding = respones.apparent_encoding
    bfStr = BeautifulSoup(respones.text,'lxml')
    content = bfStr.find_all('dl',class_ = 'panel-body panel-chapterlist')
    a_mark = BeautifulSoup(str(content[0]),'lxml')  #再次解析内容
    a = a_mark.find_all('a')     #找到a标签的内容
    #遍历标签
    for aStr in a:
        # print(aStr.string,spiderUrl+aStr.get('href'))
        print(aStr.get('title'), spiderUrl + aStr.get('href'))



    # print(content[0])



