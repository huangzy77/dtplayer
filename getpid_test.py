import psutil
import re

 
def processinfo(x):
    p = list(psutil.process_iter())
    pid=0
    for r in p:
        aa = str(r)
        f = re.compile(x,re.I)
        if f.search(aa):
            pid=aa.split('pid=')[1].split(',')[0]  
            #print aa.split('pid=')
    return pid  
print processinfo("sslocal")