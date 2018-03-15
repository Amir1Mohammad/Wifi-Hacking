__author__ = "Amir Mohammad"

import subprocess

command_one = "netsh wlan show profiles"
var = "All User Profile"
wifi_list=[]

a = subprocess.check_output(command_one.split(" ")).decode('utf-8').split('\n')
a = [i for i in a if "All User Profile" in i]
c=0
for i in a:
        
        try:
                t = i.split(':')[1].replace('\r', '')
                t = t.strip()
                resault = subprocess.check_output(['netsh','wlan','show','profile',t,'key=clear']).decode('utf-8').split('\n')
                resault = [b for b in resault if "Key Content" in b]
                
                print t," : ",resault
        #print resault
        except:
                print ""
