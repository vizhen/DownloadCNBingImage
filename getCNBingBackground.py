#!/usr/bin/python
# coding=utf-8
import urllib

def readCNBingPage():
    return urllib.urlopen("http://cn.bing.com").read()
    
def getImageUrl(content):
    tagpos = content.find("g_img=")
    if tagpos <> -1:
      imageStart = content.find("'", tagpos)
      imageEnd = content.find("',", tagpos)
      return content[imageStart + 1:imageEnd]
    if tagpos == -1:
      print "解析标签失败，可能页面格式已经改变!"
      return "图片URL解析失败!"
      
def downLoadImage(url):
    if url.startswith("http"):
      picName = url[url.rfind("/") + 1:]
      print "准备下载:" + url
      urllib.urlretrieve(url, picName)
      print "保存 " + picName + " 在当前路径下!"
    else:
      print url + " 不是一个正确的图片URL地址!"
    
if __name__ == '__main__':
   downLoadImage(getImageUrl(readCNBingPage()))
       
   
