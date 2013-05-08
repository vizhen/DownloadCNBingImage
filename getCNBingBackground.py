#!/usr/bin/python

import urllib

def readCNBingPage():
    return urllib.urlopen("http://cn.bing.com").read()
    
def getImageUrl():
    content = readCNBingPage()
    tagpos = content.find("g_img=")
    if tagpos <> -1:
      imageStart = content.find("'", tagpos)
      imageEnd = content.find("',", tagpos)
      return content[imageStart + 1:imageEnd]
    if tagpos == -1:
      print "Page format is change!Can not find imag url!"
      return "Image Url not found!"
      
def downLoadImage(url):
    if url.startswith("http"):
      picName = url[url.rfind("/") + 1:]
      print "Downloading:" + url
      urllib.urlretrieve(url, picName)
      print "Saved " + picName + " in current path!"
    else:
      print url + " is not a url!"
    
downLoadImage(getImageUrl())
       
   