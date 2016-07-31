#browser bomb by JackCDK
#adding your name to the credits dosn't make you a programmer.
import webbrowser
import time
from itertools import repeat

#variables
hlink = "http://"
websi = "www.google.com" 
num = 1

try: input = raw_input
except NameError: pass


t1 = "===========[python2 edition]========="
t2 = "   ___         ___            _      "
t3 = "  | _ )  ___  | _ ) ___ _ __ | |__   "
t4 = "  | _ \ |___| | _ \/ _ \ '  \| '_ \  "
t5 = "  |___/       |___/\___/_|_|_|_.__/  "
t6 = "                                     "
t7 = "        Browser Bomb By JackCDK      "
ta = "               [V1.0.6]              "
tb = "        [www.Jackcdk.comxa.com]      "
t8 = "====================================="
t9 =""

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(ta)
print(tb)
print(t8)
print(t9)


websi = input("[?] What site do you want to use?:")
while True:
    try:
        num = int(input("[?]How many times should your site open?: "))
    except ValueError:
        print("[-] Sorry, I didn't understand that.")
        #try again
        continue
    else:
        #exit loop
        break
time.sleep(2)
for word in ['spaming'] * num:
        webbrowser.open(hlink+websi)
        time.sleep(0.4)

