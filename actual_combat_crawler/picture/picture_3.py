# -*- coding:utf-8 -*-
# @Time : 2024/7/17 23:59
# Auther : shenyuming
# @File : picture_3.py
# @Software : PyCharm
'''
re -- 图片爬取 -- 所有图片在一个文件夹
'''
import requests,re,os,sys

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
pic_path = f'../../text_crawler/picfilebian/'

#获取图片所在地址
def get_picture(picUrl):
    html = requests.get(url=picUrl,headers=headers).text
    urls = re.findall('<li><a href="(.*?)" target="_blank">.*?</a></li>',html)

    for url in urls:
        pic_url = 'https://pic.netbian.com'+url
        htmlPic = requests.get(pic_url,headers=headers)
        htmlPic.encoding = htmlPic.apparent_encoding
        htmlPic = htmlPic.text
        download_picture(htmlPic)

#存储图片
def download_picture(htmlPic):
    pic_paths = re.findall('<img src="(.*?)" data-pic=".*?" alt=".*?" title=".*?">',htmlPic) #['/uploads/allimg/240724/235218-17218363382899.jpg']
    pic_name = re.findall('<img src=".*?" data-pic=".*?" alt=".*?" title="(.*?)">', htmlPic)
    if not os.path.exists(pic_path):
        os.makedirs(pic_path)  # 文件夹不存在就创建

    for name in pic_name:
        new_name = name.replace("['","").replace("']","").replace(" ","")
        for _path in pic_paths:
            new_pic_path = 'https://pic.netbian.com/' + _path   #https://pic.netbian.com//uploads/allimg/240825/222048-17245956489a81.jpg
            respones = requests.get(new_pic_path,headers=headers).content   #真实地址用content
            with open(str(pic_path+'/'+new_name+'.jpg'),'wb')as f:
                f.write(respones)
    # 循环读取
    #下一页
    # nextPage = re.findall("<a href='(.*?)'>下一页</a>",htmlPic)
    # if nextPage:
    #     for url in nextPage:
    #         _url = 'https://pic.netbian.com/'+url
    #         content = requests.get(url=_url,headers=headers).text
    #         download_picture(content)

#开始
def start_pict(urlPic):
    for i in range(1,5):
        if i ==1:
            url = urlPic + 'index.html'
            print("url:",url)
            get_picture(url)
        else:
            url = urlPic+'index_'+str(i)+'.html'
            print("url2:",url)

            get_picture(url)


if __name__ == '__main__':
    # get_picture('https://pic.netbian.com/4kmeinv/')   #https://pic.netbian.com/4kmeinv/index_2.html
    start_pict('https://pic.netbian.com/4kmeinv/')