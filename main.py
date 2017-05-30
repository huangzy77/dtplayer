# -*- coding:utf-8 -*- 
import os
import getInfo
import time
from multiprocessing import Process,Queue
import subprocess
from time import sleep
import requests


def is_connected(q):
    print "is p {}".format(os.getppid())
    print "is {}".format(os.getpid())
    count=0
    while True:
        count+=1
        try:
            print("The {} times test!".format(count))
            resp = requests.get('http://www.google.com', proxies=dict(http='socks5://localhost:1080',https='socks5://localhost:1080'),timeout=10)
            if(resp.status_code==200):
                print("Everything is oK!")
                q.put(1)
                sleep(20)
            else:
                print("Something wrong! Status Code is {}".format(resp.status_code))
                q.put(0)
                sleep(20)
        except Exception,e:  
            #print Exception,":",e
            print('Something wrong! Restart!')
            q.put(0)
            sleep(20)

def ss_start(q):
    print "ss p {}".format(os.getppid())
    print "ss {}".format(os.getpid())
    try:
        json_path=os.getcwd()
        getInfo.makejson(json_path)
        #print("执行{}".format(os.getpid()))
        obj=subprocess.Popen("sslocal -c "+json_path+"/dtplayer.json",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        print('ss is Run!objpid {}'.format(obj.pid))
        '''
        lines=obj.stdout.readlines()       
        if not lines or len(lines)==0:
            lines=obj.stderr.readlines()
        '''

        
        #print lines
        while True:#监听is子进程传来的消息，０为需要重启ss进程，１为正常          
            value=q.get(True)
            print value
            if value==0:
                obj.kill()
                ss_start(q)
    except Exception,e:
        print('ss is wrong!')  
        print Exception,":",e


if __name__ == "__main__":
    try:
        #print "main {}".format(os.getpid())
        q=Queue()
        p_ss=Process(target=ss_start,args=(q,))
        p_is=Process(target=is_connected,args=(q,))
        p_ss.start()
        p_is.start()
       # p_ss.join()#这个是用来等待子进程结束后回收子进程的
     
        #p_is.join()
    except Exception,e:  
        print Exception,":",e
       
       


    
