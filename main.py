__author__ = "Amir Mohammad"

import subprocess

command_one = "netsh wlan show profiles"
var = "All User Profile"


a = subprocess.check_output(command_one.split(" ")).decode('utf-8').split('\n')
a = [i for i in a if "All User Profile" in i]
c=0
for i in a:
        c+=1
        
        t = i.split(':')[1].replace('\r', '')
        t = t.strip()
        print t
        



#print i
#resault = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('\n')
#resault = [b for b in resault if "Key Content" in b]

