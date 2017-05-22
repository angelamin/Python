# -*- coding: utf-8 -*-

import bs4
import urllib2
from bs4 import BeautifulSoup

#解决ascill编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 根据html网页字符串创建BeautifulSoup对象
content = urllib2.urlopen('http://www.cnblogs.com/dolphinX/p/4381855.html').read()
# print content
soup = BeautifulSoup(content,'html.parser')

# print soup.p.string  #只会寻找满足的第一个p标签

result = []

#获取所有的p标签
arrs = soup.find_all('p')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)   #将得到的每个p标签的内容存到result中去

#获取所有的a标签
arrs = soup.find_all('a')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)   #将得到的每个a标签的内容存到result中去

arrs = soup.find_all('h3')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)

arrs = soup.find_all('div')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)

arrs = soup.find_all('h1')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)

arrs = soup.find_all('b')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)

arrs = soup.find_all('li')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)

arrs = soup.find_all('article')
for arr in arrs:
    if arr.string != None:
        result.append(arr.string)

# print result
# result.remove(None)

#将爬到的文字保存到本地文件里
filePath = "/Users/xiamin/Downloads/Python/Xinan/python-function/texts.txt"
f = open(filePath,'a')    #以追加的模式

for re in result:
    f.write(re)
    f.write("\n")
    print re

f.close()




if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
