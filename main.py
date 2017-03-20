# -*- coding:utf-8 -*- 
import os
import getInfo
from threading import Timer
from operator import or_




def isConnected(ip_str):#判断获取的ＩＰ是否还有效果
    output=os.popen("ping -c 1 -w 2 %s" % (ip_str)).read().split("\n")
    if "1 packets transmitted, 1 received, 0% packet loss, time 0ms" in output:
        return 1
    else:
        return 0

def run_server(): 
    '''
    if processinfo("sslocal")==0:
        getInfo.makejson(json_path)
        os.system("sslocal -c "+json_path+"/dtplayer.json") 
    else:
        os.system("command")
        getInfo.makejson(json_path)
        os.system("sslocal -c "+json_path+"/dtplayer.json") 
        '''
    flag_num=0#记录第几次运行
    data_dic0,data_dic1=getInfo.getData()
    ip_str=data_dic0["server"]
    json_path=os.getcwd() #确定shadow.json目录
    while (isConnected(ip_str)==0 or flag_num==0) :
        os.system("pkill sslocal")
        getInfo.makejson(json_path)
        os.system("sslocal -c "+json_path+"/dtplayer.json")
        flag_num+=1

    
  
if __name__ == "__main__":
    try:
        run_server()  
    except Exception,e:  
        print Exception,":",e
       


    