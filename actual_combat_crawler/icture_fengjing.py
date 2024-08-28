# -*- coding:utf-8 -*-
# @Time : 2024/8/28 21:38
# Auther : shenyuming
# @File : icture_fengjing.py
# @Software : PyCharm
import os
import urllib.request
from  urllib import request
import re,chardet
from urllib.error import HTTPError

'''
urllib ,re 读取彼岸网风景图片，
'''

class DownladPicture:
     def __init__(self,path):
         self.path = path
    # 读取图片内容链接
     def get_picture(self,url,headers):
         req = urllib.request.Request(url=url,headers=headers)
         content= urllib.request.urlopen(req).read()
         return content
         # with request.urlopen(url) as f:
         #     content = f.read()
         #     return content
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

         #保存图片
         i = 0
         http = 'https://pic.netbian.com'
         for image in image_list:
             print(f'{http}'+ image)
             print(f'{self.path}'+'%s.jpg' % i)
             try:
                urllib.request.urlretrieve(f'{http}'+ image, f'{self.path}'+'%s.jpg' % i)
                i += 1
             except HTTPError as e:
                 if e.code == 403:
                     print("HTTP Error 403: Forbidden")
                 else:
                     print(f"HTTP Error: {e.code}")
             except Exception as e:
                 print(f"An error occurred: {e}")


     # def start_download(self,url,headers):
     #     content = self.get_picture(url,headers)
     #     self.creading_img(content)

if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kfengjing/'
    path = f'../text_crawler/picfilefengjing/'
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    dow = DownladPicture(path)
    con = dow.get_picture(url,headers)
    dow.creading_img(con)