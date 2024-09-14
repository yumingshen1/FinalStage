# -*- coding:utf-8 -*-
# @Time : 2024/6/6 22:30
# Auther : shenyuming
# @File : xiashuo_3.py
# @Software : PyCharm

import sys,time
import threading

import requests
from bs4 import BeautifulSoup
from threading import Thread
"""
先准备url,headers,  存放name,url,数量，的变量；
请求URL，获的文本，  BeautifulSoup处理文本，
获得内容==》查找在那个标签内
再找具体内容，将所需要的内容循环读取存入变量；

再从获取到的URL中读取文本信息，注意编码格式，还是以BeautifulSoup处理文本。
查找具体内容， 用一些内置函数处理所需要的数据和不需要的数据。
将处理后的内容存入临时变量并返回

处理写的方法：文件路径，数据
循环写入
"""
class Downloader():
    def __init__(self):
        self.serverUrl = 'https://www.biqukan.co/'           #首页
        self.targetUrl = 'https://www.biqukan.co/book/110254/'  #第一页全部章节
        self.indexgetUrl = 'https://www.biqukan.co/book/110254/index_' #从第二页开始+1   2.html
        self.hearders = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        self.proxy = '127.0.0.1:9180'  #这里写代理的ip及端口
        self.proxies = {
            'http': 'http://' + self.proxy,
            'https': 'https://' + self.proxy
        }
        self.name = []
        self.urls = []
        self.nums = 0 #章节数


    def get_download_url(self):
        """
        获得第一页的name和url
        :return:
        """
        respones = requests.get(url=self.targetUrl,headers=self.hearders)
        respones.encoding = respones.apparent_encoding
        bfStr = BeautifulSoup(respones.text, 'lxml')
        content = bfStr.find_all('dl', class_='panel-body panel-chapterlist')
        a_mark = BeautifulSoup(str(content[0]), 'lxml')  # 再次解析内容
        a = a_mark.find_all('a')  # 找到a标签的内容
        self.nums = len(a)
        # 遍历标签
        for aStr in a:
            self.name.append(aStr.get('title'))
            self.urls.append(self.targetUrl + aStr.get('href'))
            # print(aStr.get('title'), self.targetUrl + aStr.get('href'))


    def get_download_url_index(self):
        """
        获得第二页以及之后的 name和url
        :return:
        """
        for i in range(2, 82):
            try:
                url_index = self.indexgetUrl + f'{i}.html'
                respones = requests.get(url=url_index, headers=self.hearders)
                time.sleep(2)
                respones.encoding = respones.apparent_encoding
                bfStr = BeautifulSoup(respones.text, 'lxml')
                content = bfStr.find_all('dl', class_='panel-body panel-chapterlist')
                a_mark = BeautifulSoup(str(content[0]), 'lxml')  # 再次解析内容
                a = a_mark.find_all('a')  # 找到a标签的内容
            # 遍历标签
                for aStr in a:
                    self.nums +=1
                    self.name.append(aStr.get('title'))
                    self.urls.append(self.targetUrl + aStr.get('href'))
                    # print(aStr.get('title'), self.targetUrl + aStr.get('href'))
            except requests.exceptions.ConnectionError as r:
                r.status_code = "Connection refused"

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
        content = content.replace("    ","").replace('br /> ',"").replace('p;',"").replace('p;  ',"").replace("p;   ","").replace("; ","").strip()
        contents = name+content
        return contents

    def writer(self,path,text_one,text_two):
        with open(path,'w+',encoding='utf-8') as f:
            # f.write(name +'\n' )
            # f.write(text +'\n')
            f.writelines(text_one)
            f.write('\n')
            f.writelines(text_two)
            f.seek(0)




if __name__ == '__main__':

    dler = Downloader()
    # threads = []
    # t1 = threading.Thread(target=dler.get_download_url)
    # threads.append(t1)
    # t2 = threading.Thread(target=dler.get_download_url_index)
    # threads.append(t2)
    # for t in threads:
    #     t.start()
    dler.get_download_url()
    # dler.get_download_url_index()
    print("*************下载中**************")
    for url in range(dler.nums):
        dler.writer(f'../text_crawler/textFile/{dler.name[url]}.txt',dler.get_content_one(dler.urls[url]),dler.get_content_two(dler.nums,dler.urls[url]))
        sys.stdout.write('已下载：%.3f%%' % float(url/dler.nums)+'\r')
        sys.stdout.flush()
    print('执行完毕！！！')