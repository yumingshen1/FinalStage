# -*- coding:utf-8 -*-
# @Time : 2024/6/6 22:30
# Auther : shenyuming
# @File : xiaoshuo_3.py
# @Software : PyCharm
import sys

import requests
from bs4 import BeautifulSoup

class Downloader():
    def __init__(self):
        self.serverUrl = 'https://www.biqukan.co/'           #首页
        self.targetUrl = 'https://www.biqukan.co/book/110254/'  #全部章节
        self.name = []
        self.urls = []
        self.nums = 0 #章节数

    def get_download_url(self):
        respones = requests.get(url=self.targetUrl)
        respones.encoding = respones.apparent_encoding
        bfStr = BeautifulSoup(respones.text, 'lxml')
        content = bfStr.find_all('dl', class_='panel-body panel-chapterlist')
        a_mark = BeautifulSoup(str(content[0]), 'lxml')  # 再次解析内容
        a = a_mark.find_all('a')  # 找到a标签的内容
        self.nums = len(a)
        print('nums数量：',self.nums)
        # 遍历标签
        for aStr in a:
            self.name.append(aStr.get('title'))
            self.urls.append(self.targetUrl + aStr.get('href'))
            # print(aStr.get('title'), self.targetUrl + aStr.get('href'))

    def get_content_one(self,targetUrl):
        respones = requests.get(url=targetUrl)
        respones.encoding = respones.apparent_encoding
        htmlStr = respones.text
        bfStr = BeautifulSoup(htmlStr, 'lxml')
        bfStr.find_all('div',class_='clear')
        name = bfStr.text.split('_重生之都市仙尊', 1)[0]
        content = bfStr.text.split('最快更新重生之都市仙尊最新章节！', 1)[1]

        end_content = '... -->>本章未完'
        end_content2 = '上一页章节目录下一章请安装我们的客户端'
        for i in content:
            if i in end_content:
                content = content.split(end_content, 2)[0]
            elif i in end_content2:
                content = content.split(end_content2, 2)[0]
        print(name + content)
        content = content.replace("    ","").strip()
        contents = name+content
        return contents

    def get_content_two(self,n,targetUrl):
        targetUrlTwo = targetUrl.split('.html')[0]
        targetUrlTwo = targetUrlTwo+'_'+f'{n}'+'.html'
        respones = requests.get(url=targetUrlTwo)
        respones.encoding = respones.apparent_encoding
        htmlStr = respones.text
        bfStr = BeautifulSoup(htmlStr, 'lxml')
        bfStr.find_all('div',class_='clear')
        print('bfstr:',bfStr.text)
        name = bfStr.text.split('_重生之都市仙尊', 1)[0]
        content = bfStr.text.split('最快更新重生之都市仙尊最新章节！', 1)[1]
        print('name:',name)
        end_content = '... -->>本章未完'
        end_content2 = '上一页章节目录下一章请安装我们的客户端'
        for i in content:
            if i in end_content:
                content = content.split(end_content, 2)[0]
            elif i in end_content2:
                content = content.split(end_content2, 2)[0]
        print(name + content)
        content = content.replace("    ","").replace('br /> ',"").replace('p;',"").replace('p;  ',"").replace("p;   ","").replace("; ","").strip()
        contents = name+content
        return contents

    def writer(self,name,path,text_one,text_two):
        with open(path,'w+',encoding='utf-8') as f:
            f.write(name +'\n' )
            # f.write(text +'\n')
            f.writelines(text_one)
            f.write('\n')
            f.writelines(text_two)
            f.seek(0)


if __name__ == '__main__':
    dler = Downloader()
    dler.get_download_url()
    # dler.get_content_two(1,'https://www.biqukan.co/book/110254/35672400_2.html')
    print("*************下载中**************")
    page = 1
    for url in range(dler.nums):
        dler.writer(dler.name[url],f'../text_crawler/textFile/第{page}章.txt',dler.get_content_one(dler.urls[url]),dler.get_content_two(dler.nums,dler.urls[url]))
        sys.stdout.write('已下载：%.3f%%' % float(url/dler.nums)+'\r')
        sys.stdout.flush()
        page +=1
        # if page == 3:
        #     break
    print('执行完毕！！！')