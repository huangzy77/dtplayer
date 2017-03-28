# -*- coding:utf-8 -*- 
import os
import getInfo
import time
from multiprocessing import Process, Queue
from operator import or_

#开两个线程，一个监视网络是否连接，一个用于重启sslocal


def isConnected():#判断获取的ＩＰ是否还有效果
    counter=0
    temp=0
    data_dic0,data_dic1=getInfo.getData()
    ip_str=data_dic1["server"]
    while True:
        output=os.popen("ping -c 1 -w 2 %s" % (ip_str)).read().split("\n")
        if "1 packets transmitted, 1 received, 0% packet loss, time 0ms" in output:
            values=1
        else:
            values=0
        time.sleep(2)
        counter+=1
        temp=temp+values
        if counter>=5:
            print temp
            if temp<=2:
                restart_server()#连续3次ping不通，就重启服务
            counter=0
            temp=0


def start_server():
        json_path=os.getcwd()
        getInfo.makejson(json_path)
        os.popen("sslocal -c "+json_path+"/dtplayer.json")

def restart_server(): 
        os.system("pkill sslocal")
        start_server()



#确定shadow.json目录

  
if __name__ == "__main__":
    try:
        
        p_isConnected=Process(target=isConnected)
        p_isConnected.start()
        p_startserver=Process(target=start_server)
        p_startserver.start()
        p_isConnected.join()
        p_startserver.join()          
                
    except Exception,e:  
        print Exception,":",e
       


    