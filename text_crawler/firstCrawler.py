# -*- coding:utf-8 -*-
# @Time : 2024/6/3 22:00
# Auther : shenyuming
# @File : firstCrawler.py
# @Software : PyCharm

import requests,io
import pandas as pd
from io import StringIO


class TextCrawlerOne:
    url = 'http://finance.sina.com.cn/zt_d/subject-1667873035/'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "UOR=www.baidu.com,finance.sina.com.cn,; SINAGLOBAL=120.244.200.32_1717420810.22218; Apache=120.244.200.32_1717420810.22220; ULV=1717420865262:2:2:2:120.244.200.32_1717420810.22220:1717420809883",
        "Host": "finance.sina.com.cn",
        "If-None-Match": "W/\"6391c038-35a21\"V=32179E4F",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    def textCrawler_1(self):
        response = requests.get(TextCrawlerOne().url,headers=TextCrawlerOne().headers)
        #显示指定编码-1
        # response.encoding = 'utf-8'
        # print('以字符串形式打印:',response.text)

        #显示指定编码-2， 以字节形式拿到内容
        # print('以字符串形式打印:',response.content.decode('utf-8'))

        #隐式指定编码-3 ,  response.apparent_encoding == 网页指定的编码 meta标签
        response.encoding = response.apparent_encoding
        print(response.text)


    def textCrawler_2(self):
        response = requests.get(TextCrawlerOne().url, headers=TextCrawlerOne().headers)
        response.encoding = response.apparent_encoding
        pd.read_html(response.text)[0].to_csv(path_or_buf='./textFile/data.csv',encoding='utf-8-sig',index=False)
        # print(pd.read_html(response.text)[0])

if __name__ == '__main__':
    TextCrawlerOne().textCrawler_2()
