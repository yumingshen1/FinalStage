# -*- coding:utf-8 -*-
# @Time : 2024/8/27 20:33
# Auther : shenyuming
# @File : picture_tieba.py
# @Software : PyCharm

import urllib.request
from urllib import request
import re,os

'''
使用urlib.request 配合re ,爬取图片

re.compile(r'匹配字符串')
'''
pic_path = f'../../text_crawler/picfiletieba/'

#读取图片内容链接
def get_pic(url):
    with request.urlopen(url) as f:
        content = f.read()
        # print(content)
        ##查看headers
        # for k,v in f.getheaders():
        #     print('%s:%s' % (k,v))
        return content

#获取图片内容并下载
def create_img(content):
    # regRsult = re.compile(r'src="(.*?.jpg)" pic_ext')
    regRsult = re.compile(r'src="(.*?.jpg)" pic_ext=".*?"') #编译

    content = content.decode('utf-8') #字节流转化为字符串
    image_list = re.findall(regRsult,content)

    if not os.path.exists(pic_path):
        os.makedirs(pic_path)  # 文件夹不存在就创建
    #保存图片
    i=0
    for image in image_list:
        urllib.request.urlretrieve(image,f'{pic_path}'+'/%s.jpg' % i)
        i+=1

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/2555125530'
    con = get_pic(url)
    create_img(con)