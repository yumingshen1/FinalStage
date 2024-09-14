# -*- coding:utf-8 -*-
# @Time : 2024/6/5 21:54
# Auther : shenyuming
# @File : xiaoshuo_1.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url1 = 'https://www.biqukan.co/book/110254/35672400.html'
    url2 = 'https://www.biqukan.co/book/110254/35672401.html'
    url3 = 'https://www.biqukan.co/book/110254/35672401_2.html'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "cookie": "Hm_lvt_feb1ff39117c29e8b956edcbc9750dc6=1717595641; clickbids=110254,74444; jieqiVisitId=article_articleviews%3D110254%7C74444; Hm_lpvt_feb1ff39117c29e8b956edcbc9750dc6=1717596816",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    respones = requests.get(url=url3)
    respones.encoding = respones.apparent_encoding
    htmlStr = respones.text
    bfStr = BeautifulSoup(htmlStr,'lxml') #使用lxml方式解析
    bfStr.find_all('div',class_='clear') # 处理div标签。 获取 <div .... id="content">内容的东西 ，calss_ 自定义的参数(可换)的值是标签calss的值，看情况取那个class
    #bfStr.text.replace('\xa0'*8,'\n\n') #替换<br>标签
    name = bfStr.text.split('_重生之都市仙尊',2)[0]
    content = bfStr.text.split('最快更新重生之都市仙尊最新章节！',2)[1]

    end_content = '... -->>本章未完'
    end_content2 = '上一页章节目录下一章请安装我们的客户端'
    # print('未处理：',content)
    for i in content:
        if i in end_content:
            content = content.split(end_content,2)[0]
        elif i in end_content2:
            content = content.split(end_content2,2)[0]
    print(name+content)
