# -*- coding:utf-8 -*- 
import os
import getInfo
from threading import Timer

json_path=os.getcwd() #确定shadow.json目录


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
    os.system("pkill sslocal")
    getInfo.makejson(json_path)
    os.system("sslocal -c "+json_path+"/dtplayer.json")
    t = Timer(3600, run_server)  
    t.start() 
    
  
if __name__ == "__main__":
    try:
        run_server()  
    except Exception,e:  
        print Exception,":",e
       


    