# -*- coding: utf-8 -*-
# @Time    : 2024/9/12 10:50
# @Author  : shenyuming
# @FileName: video_1.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#主页地址
serverurl = 'http://www.qmxq.cc/'
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
#网页地址
url = 'http://www.qmxq.cc/anime/14396/'
html = requests.get(url=url,headers=headers).text
soup = BeautifulSoup(html,'html.parser')
#找到class=movurl的div下的所有a标签
movUrls = soup.find_all('div',class_='movurl')[0].find_all('a')

#存储url及name
mov_url = []
mov_name = []
for u in movUrls:
    mov_url.append(u.get("href"))
    mov_name.append(u.get('title'))
#拼接并获取视频完成url
for index,(item1,item2) in enumerate(zip(mov_name, mov_url)):
    # name,url= item1,serverurl+item2
    # print(name,url)
    mov_url[index] = serverurl+item2
    mov_name[index] = item1
    print(mov_url[index],mov_name[index])

#获取视频播放链接-4mp
videos= []
videos_title = []

for u in mov_url:
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.get(u)
    soup = BeautifulSoup(html,'html.parser')
    video_name = soup.find('title').string.split('-')[0]
    print(video_name)

    driver.switch_to.frame('')
