# -*- coding:utf-8 -*- 
import requests
import os
from time import sleep
count=0
while True:
    count+=1
    try:
        print("The {} times test!".format(count))
        resp = requests.get('http://www.google.com', proxies=dict(http='socks5://localhost:1080',https='socks5://localhost:1080'),timeout=10)
        if(resp.status_code==200):
            print("Everything is oK!")
            sleep(10)
        else:
            print("Something wrong! Status Code is {}".format(resp.status_code))
            os.popen("./google.sh")
    except Exception,e:  
        print Exception,":",e
        print('Something wrong! Restart!')
        os.popen("./google.sh")
        sleep(10)

