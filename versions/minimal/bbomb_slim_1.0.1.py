#browser bomb by JackCDK
#adding your name to the credits dosn't make you a programmer.
import webbrowser
import time
from itertools import repeat

#variables
hlink = "http://"
websi = "www.google.com" 

print "browserbomb minimal edition [V1.0.1m]"

websi = raw_input("[?] What site do you want to use?:")

snum = int(input("[?] How many times do you want to spam your pc?: "))
time.sleep(10)
for word in ['spaming'] * snum:
    webbrowser.open(hlink+websi)
    time.sleep(0.4)
    