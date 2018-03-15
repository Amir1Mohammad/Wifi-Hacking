__author__ = "Amir Mohammad"

import subprocess
file_obj = open("req.txt", "w")
command_one = "netsh wlan show profiles"
var = "All User Profile"

a = subprocess.check_output(command_one.split(" ")).decode('utf-8').split('\n')
a = [i for i in a if "All User Profile" in i]
counter=0
for i in a:
        counter+=1
        try:
                t = i.split(':')[1].replace('\r', '')
                t = t.strip()
                resault = subprocess.check_output(['netsh','wlan','show','profile',t,'key=clear']).decode('utf-8').split('\n')
                resault = [b for b in resault if "Key Content" in b]
                end = str(resault).split("Key Content")[1].strip()
                file_obj.write(t+end+"\n")
                print t,end
                
        #print resault
        except:
                None


file_obj.close()
