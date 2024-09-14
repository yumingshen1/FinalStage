# -*- coding:utf-8 -*-
# @Time : 2024/6/30 00:17
# Auther : shenyuming
# @File : picture_1.py
# @Software : PyCharm
'''
正则提取使用
图片爬取
'''
import requests,re,os
#一级域名
url_traget = 'https://pic.netbian.com/4kmeinv/'
#二级域名
url_p = 'https://pic.netbian.com'
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
respones = requests.get(url=url_traget,headers=headers)
html = respones.text
# print(html)
urlArry = re.findall('<li><a href="(.*?)" target="_blank">.*?</a></li>',html)
for url in urlArry:
    #三级域名
    pic_url = url_p+url
    print('访问图片html:',pic_url)
    #请求图片地址
    resp = requests.get(url=pic_url,headers=headers)
    resp.encoding=resp.apparent_encoding
    pic_html = resp.text
    #文件夹名
    headerName = re.findall('<h1>(.*?)</h1>',pic_html)
    newHeaderName = str(headerName).replace("['","").replace("']","").replace(" ","")
    #存放路径
    pic_path = f'../../text_crawler/{newHeaderName}'
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    #读取图片具体路径
    pic_content = re.findall('<img src="(.*?)" data-pic=".*?" alt=".*?" title=".*?">',pic_html)
    #读取图片名字
    pic_name = re.findall('<img src=".*?" data-pic=".*?" alt=".*?" title="(.*?)">', pic_html)

    for name in pic_name:
        fileName = name.split(' ',1)[0]
        for pic in pic_content:
            pic = url_p+pic
            picres = requests.get(pic,headers=headers)
            with open(str(pic_path)+'/'+fileName+'.jpg','wb') as f:
                f.write(picres.content)


