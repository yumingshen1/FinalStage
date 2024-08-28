# -*- coding:utf-8 -*-
# @Time : 2024/7/17 22:43
# Auther : shenyuming
# @File : picture_2.py
# @Software : PyCharm

'''
 re -- 图片爬取--每个地址图片存到一个文件夹
'''
import requests,re,os

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
pic_path = f'../text_crawler/picfile/'

#获取图片所在地址
def get_picture(picUrl):
    html = requests.get(url=picUrl,headers=headers).text
    urls = re.findall('<li><a href="(.*?)" target="_blank">.*?</a></li>',html)
    for url in urls:
        pic_url = 'https://pic.netbian.com'+url
        htmlPic = requests.get(pic_url,headers=headers)
        htmlPic.encoding = htmlPic.apparent_encoding
        htmlPic = htmlPic.text
        head_name = re.findall('<h1>(.*?)</h1>',htmlPic)
        new_head_name = str(head_name).replace("['","").replace("']","").replace(" ","")
        path = pic_path+f'{new_head_name}'
        if not os.path.exists(path):
            os.makedirs(path) #文件夹不存在就创建
        download_picture(htmlPic,path)


def download_picture(htmlPic,path):
    pic_paths = re.findall('<img src="(.*?)" data-pic=".*?" alt=".*?" title=".*?">',htmlPic)
    pic_name = re.findall('<img src=".*?" data-pic=".*?" alt=".*?" title="(.*?)">', htmlPic)

    for name in pic_name:
        new_name = name.split(" ",1)[0]
        for _path in pic_paths:
            new_pic_path = 'https://pic.netbian.com/' + _path
            respones = requests.get(new_pic_path,headers=headers).content
            with open(str(path+'/'+new_name+'.jpg'),'wb')as f:
                f.write(respones)



if __name__ == '__main__':
    get_picture('https://pic.netbian.com/4kmeinv/index.html')

