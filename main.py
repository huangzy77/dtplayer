# -*- coding:utf-8 -*- 
import os
import getInfo
import time
from multiprocessing import Process,Pipe
from time import sleep

#开两个线程，一个监视网络密码端口是否更改，一个用于重启sslocal


def isConnected(pipe):#一个监视网络密码端口是否更改
    data_dic0_st,data_dic1_st=getInfo.getData()
    count=0
    while True:
        try:
            count+=1
            data_dic0,data_dic1=getInfo.getData()
            print count
            sleep(1)
            if (data_dic0==data_dic0_st and data_dic1==data_dic1_st):
                print("系统检测正常,传递值０:")
                pipe.send(0)
                count=0
            if count>=20:
                print("更新密码、端口中...")
                os.popen("pkill sslocal")
                pipe.send(1)
                count=0
        except Exception,e:  
            print Exception,":",e


def start_server(pipe):
    json_path=os.getcwd()
    getInfo.makejson(json_path)
    print("执行")
    os.popen("sslocal -c "+json_path+"/dtplayer.json")
    while True: #监听另外一个进程传来的消息
        if(pipe.recv()==1):
            print("重启啦...")
            start_server(pipe)




if __name__ == "__main__":
    try:
        pipe=Pipe()
        p_isConnected=Process(target=isConnected, args=(pipe[0],))
        p_startserver=Process(target=start_server, args=(pipe[1],)) 
        p_isConnected.start()
        p_startserver.start()
        p_isConnected.join()
        p_startserver.join() 


   
                
    except Exception,e:  
        print Exception,":",e
       
       


    