# -*- coding:utf-8 -*- 
#from selenium import webdriver
import urllib2
import json 
from bs4 import BeautifulSoup
from bs4.builder import HTML

def getHtml(url):#爬取html
    try:
        req=urllib2.Request(url)
        req.add_header('Referer', 'https://www.kejiss.com/page/testss.html')
        req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
        r=urllib2.urlopen(req)
        html=r.read()
    except:
        return(getHtml(url))
    return html

def getData():#从html中提出账号、密码等信息
    html=getHtml('https://www.kejiss.com/page/testss.html')
    soup=BeautifulSoup(html,"html.parser")
   #获取ＩＰ和加密方式
    info_tag0=soup.select('div[class="testvpnitem"]')[0]
    info_tag1=soup.select('div[class="testvpnitem"]')[1]
    ip_str0=info_tag0.findAll('span')[0].string #第一个账号的ＩＰ
    ip_str1=info_tag1.findAll('span')[0].string #第二个账号的ＩＰ
    encrypt_str0=info_tag0.findAll('span')[1].string #第一个账号的加密方式
    encrypt_str1=info_tag1.findAll('span')[1].string #第二个账号的加密方式
    #获取端口号
    port_index0=str(info_tag0).index('端口：')
    port_index1=str(info_tag1).index('端口：')
    port_str0=str(info_tag0)[port_index0+9:port_index0+13]#第一个账号的端口号
    port_str1=str(info_tag1)[port_index1+9:port_index1+13]#第二个账号的端口号
    #获取密码
    psw_index0=str(info_tag0).index('密码：')
    psw_index1=str(info_tag1).index('密码：')
    psw_str0=str(info_tag0)[psw_index0+9:psw_index0+15]#第一个账号的密码
    psw_str1=str(info_tag1)[psw_index1+9:psw_index1+15]#第二个账号的密码
    #print ip_str0,ip_str1,encrypt_str0,encrypt_str1,port_str0,port_str1,psw_str0,psw_str1
    data_dic0={"server":ip_str0,"server_port":port_str0,"local_address":"127.0.0.1","local_port":1080,"password":psw_str0,"timeout":300,\
               "method":encrypt_str0,"fast_open":'true',"workers":5}
    data_dic1={"server":ip_str1,"server_port":port_str1,"local_address":"127.0.0.1","local_port":1080,"password":psw_str1,"timeout":300,\
               "method":encrypt_str1,"fast_open":'true',"workers":5}
    return data_dic0,data_dic1


def makejson(pathname):#将提取的信息做成json文档然后存储到制定路径
    data_dic0,data_dic1=getData()
    file=pathname+'/dtplayer.json'
    fp=open(file,'w')
    fp.write(json.dumps(data_dic1))
    fp.close()
    
data_dic0,data_dic1=getData()
print data_dic1