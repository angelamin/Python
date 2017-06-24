# -*- coding: utf-8 -*-
# 夏敏
import re
import urllib
import urllib2
import os
import requests
import time;  # 引入time模块

#抓取网页图片

#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#创建保存图片的文件夹
def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在    True
    # 不存在  Flase
    isExists = os.path.exists(path)
    if not isExists:
        print u'新建了名字叫做',path,u'的文件夹'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已经存在
        print u'名为',path,u'的文件夹已经创建成功'
        return False

# 输入文件名，保存多张图片
def saveImages(imglist,name,number):
    # print '33'
    # number = time.time()
    if number <= 300:
        for imageURL in imglist:
            # print imageURL
            if number <=300:
                splitPath = imageURL.split('.')
                fTail = splitPath.pop()
                if len(fTail) > 3:
                    fTail = 'jpg'
                fileName = name + "/" + str(number) + "." + fTail
                # 对于每张图片地址，进行保存
                try:
                    u = urllib2.urlopen(imageURL)
                    data = u.read()
                    f = open(fileName,'wb+')
                    f.write(data)
                    print u'正在保存的一张图片为',fileName
                    f.close()
                except urllib2.URLError as e:
                    print (e.reason)
                number += 1
        return number
    # elif x == 90:
    # return 6


#获取网页中所有图片的地址
def getAllImg(html,number):
    #利用正则表达式把源代码中的图片地址过滤出来
    # print '111'
    # reg = r'src="(.+?\.jpg)" pic_ext'

    # 声明一个存放所有图片网址的文件
    filePath = "/Users/xiamin/Downloads/Python/Xinan/python-function/pic-url.txt"
    f = open(filePath,'a')    #以追加的模式
    #匹配图片的地址
    reg = r'src="(http.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html) #表示在整个网页中过滤出所有图片的地址，放在imglist中
    # print imglist
    #将图片的地址写入
    for img in imglist:
        if number <= 300:
            f.write(img)
            f.write("\n")
            number+=1
    return imglist

#获取网页所有的链接
def getAllLink(url):
    #connect to a URL
    website = urllib2.urlopen(url)
    #read html code
    html = website.read()
    #use re.findall to get all the links
    links =re.findall(r'(?<=href=["])http.*?(?=["])' , html)
    return links

#创建本地保存文件夹，并下载保存图片
if __name__ == '__main__':
    html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B8%DF%C7%E5%BD%F0%C3%AB%B1%DA%D6%BD&hs=2&xthttps=000000&fr=ala&ori_query=%E9%AB%98%E6%B8%85%E9%87%91%E6%AF%9B%E5%A3%81%E7%BA%B8&ala=0&alatpl=sp&pos=0")#获取该网址网页详细信息，得到的html就是网页的源代码
    path = u'picture'
    mkdir(path) #创建本地文件夹
    number = 1

    #清空文件内容
    filePath = "/Users/xiamin/Downloads/Python/Xinan/python-function/pic-url.txt"
    f = open(filePath,'w')
    f.close()

    imglist = getAllImg(html,number) #获取图片的地址列表

    number = saveImages(imglist,path,number) # 保存图片
    url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B8%DF%C7%E5%BD%F0%C3%AB%B1%DA%D6%BD&hs=2&xthttps=000000&fr=ala&ori_query=%E9%AB%98%E6%B8%85%E9%87%91%E6%AF%9B%E5%A3%81%E7%BA%B8&ala=0&alatpl=sp&pos=0"
    linklist = getAllLink(url)
    for link in linklist:
        # print link
        html1 = getHtml(link)
        imglist1 = getAllImg(html1,number) #获取图片的地址列表
        # print '22'
        number=saveImages(imglist1,path,number) # 保存图片
        # print '44'
    f.close()
