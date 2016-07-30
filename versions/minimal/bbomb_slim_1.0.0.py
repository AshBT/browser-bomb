#browser bomb by JackCDK
#adding your name to the credits dosn't make you a programmer.
#this is the minimal version
import webbrowser
import time
from itertools import repeat

#variables
hlink = "http://"
websi = "www.google.com" 

print "browserbomb minimal edition [V1.0.0m]"

snum = int(input("[?] How many times do you want to spam your pc?: "))
time.sleep(10)
for word in ['spaming'] * snum:
    webbrowser.open(hlink+websi)
    time.sleep(0.5)
    