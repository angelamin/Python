# coding: utf-8
#下载图片

import urllib

def download():
    f = open('00000001.jpg','wb')
    f.write(urllib.urlopen('http://www.gunnerkrigg.com//comics/00000001.jpg').read())
    f.close()
if __name__ == '__main__':
    download()
