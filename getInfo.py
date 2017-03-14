# -*- coding:utf-8 -*- 
import urllib2
import sys  
from bs4 import BeautifulSoup

def getHtml(url):#
    req=urllib2.Request(url)
    req.add_header('Referer', 'https://www.ssegou.com')
    req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
    r=urllib2.urlopen(req)
    html=r.read()
    return html

def getData(html):
    soup=BeautifulSoup(html)
    ip_str=soup.findAll("IP:")
    return ip_str

h=getHtml('https://www.ssegou.com/page/testss.html')
print getData(h)