# -*- coding:utf-8 -*-
# @Time : 2024/8/28 21:38
# Auther : shenyuming
# @File : picture_fengjing.py
# @Software : PyCharm
import os,requests
import urllib.request
from random import random
import re
from urllib.error import HTTPError
import configparser
import chardet
import random
import json
import ssl
'''
urllib ,re 读取彼岸网风景图片，

urllib.request.urlretrieve请求时报错urllib.error.HTTPError: HTTP Error 403: Forbidden 解决办法:
https://blog.csdn.net/yuan2019035055/article/details/126609663
'''

class DownladPicture:
     def __init__(self,path):
         self.path = path

    # 读取图片内容链接
     def get_picture(self,url,headers):
         req = urllib.request.Request(url=url,headers=headers)
         print(type(url),type(headers))
         ssl._create_default_https_context = ssl._create_unverified_context  #忽略ssl校验
         # content= urllib.request.urlopen(req).read()

         with urllib.request.urlopen(req) as response:
             content = response.read()
         return content

     #读取图片内容并下载
     def creading_img(self,content):
         reg_result=re.compile(r'src="(.*?.jpg)" alt=".*?">')
         # 使用 chardet 检测编码
         detected_encoding = chardet.detect(content)['encoding']
         # 将字节流转换为字符串
         html_content = content.decode(detected_encoding, errors='replace')

         image_list = re.findall(reg_result,html_content)

         #创建文件路径
         if not os.path.exists(self.path):
             os.makedirs(self.path)

         #添加headers浏览器头
         opener = urllib.request.build_opener()
         ua_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
                    ]
         opener.addheaders = [('User-Agent', random.choice(ua_list))]
         i = 1
         http = 'https://pic.netbian.com'
         for image in image_list:
             try:
                 urllib.request.install_opener(opener)
                 urllib.request.urlretrieve(f'{http}' + image, f'{self.path}' + '%s.jpg' % i)
                 print(f'第{i}次执行完毕！')
                 i += 1

             except HTTPError as e:
                 if e.code == 403:
                     print("HTTP Error 403: Forbidden")
                 else:
                     print(f"HTTP Error: {e.code}")
             except Exception as e:
                 print(f"An error occurred: {e}")


     def start_download(self,url,headers):
         content = self.get_picture(url,headers)
         self.creading_img(content)

if __name__ == '__main__':
    # url = 'https://pic.netbian.com/4kfengjing/'
    # file_path = f'../text_crawler/picfilefengjing/'
    # headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config.get('settings','url')
    file_path = config.get('settings','file_path')
    headers = config.get('settings','headers')
    http = config.get('settings','http')
    ua_list = config.get('settings','ua_list')
    onfig_dict = {}
    headers_dict = json.loads(headers)
    print(headers_dict,type(headers_dict))
    # print(f'{url}',type(f'{url}'))
    # print(f'{file_path}',type(f'{file_path}'))
    # print(f'{headers}',type(f'{headers}'))
    # print(f'{http}',type(f'{http}'))
    # # print(f'{ua_list}',type(f'{ua_list}'))

    dow = DownladPicture(file_path)
    dow.start_download(url,headers_dict)