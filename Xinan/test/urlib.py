# -*- coding: utf-8 -*-
import HTMLParser
import urllib
import sys
print 'xiamin'
urlString ="http://www.python.org"
#把图像文件保存至硬盘 　　
def getImage(addr):
    u = urllib.urlopen(addr)
    data = u.read()
    splitPath = addr.split('/')
    fName = splitPath.pop()
    print"Saving %s"% fName
    f = open(fName, 'wb')
    f.write(data)
    f.close()
#定义HTML解析器 　　
class parseImages(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag =='img':
            for name,value in attrs:
                if name =='src':
                    getImage(urlString +"/"+ value)
                    #创建HTML解析器的实例 　　
                    lParser = parseImages()
                    #打开HTML文件 　　
                    u = urllib.urlopen(urlString)
                    print"Opening URL\n===================="
                    print u.info()
                    #把HTML文件传给解析器 　　l
                    Parser.feed(u.read())
                    lParser.close()
def main():
    mw = parseImages()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
