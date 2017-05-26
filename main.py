# -*- coding:utf-8 -*- 
import os
import getInfo

from time import sleep
import requests


#开两个线程，一个监视网络密码端口是否更改，一个用于重启sslocal


def isConnected(pipe):#一个监视网络密码端口是否更改
    count=0
    while True:
        count+=1
        try:
            print("The {} times test!".format(count))
            resp = requests.get('http://google.com', proxies=dict(http='socks5://localhost@1080',https='socks5://localhost@1080'))
            if(resp.status_code==200):
                print("Everything is oK!")
                pipe.send(0)
            else:
                print("Something wrong! Status Code is {}".format(resp.status_code))
                pipe.send(1)
        except:
            print('Something wrong! Restart!')
            pipe.send(1)
                    
            

    '''
    data_dic0_st,data_dic1_st=getInfo.getData()
    count=0
    while True:
        count+=1
        data_dic0,data_dic1=getInfo.getData()
        print count
        sleep(1)
        if (data_dic0==data_dic0_st and data_dic1==data_dic1_st):
            print("系统检测正常,传递值０:")
            pipe.send(0)
            count=0
        if count>=50:
            print("更新密码、端口中...")
            os.popen("killall sslocal")
            pipe.send(1)
            count=0
    '''
    
            
    


def start_server(pipe):
    json_path=os.getcwd()
    getInfo.makejson(json_path)
    print("执行")
    try:
        os.popen("sslocal -c "+json_path+"/dtplayer.json")
        '''
        while True: #监听另外一个进程传来的消息
            if(pipe.recv()==1):
                print("重启啦...")
                start_server(pipe)
            '''
    except Exception,e:  
        print Exception,":",e
        




if __name__ == "__main__":
    json_path=os.getcwd()
    getInfo.makejson(json_path)
    print("执行")
    try:
        os.popen("sslocal -c "+json_path+"/dtplayer.json")
    except Exception,e:  
        print Exception,":",e
       
       


    