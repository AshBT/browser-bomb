#browser bomb by JackCDK
#adding your name to the credits dosn't make you a programmer.
import webbrowser
import time
from itertools import repeat
import colorama
from colorama import Fore, Back, Style

#variables
hlink = "http://"
#dashd = "://"
websi = "www.google.com" 
yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

colorama.init()

t1 = "==================================="
t2 = "  ___         ___            _     "
t3 = " | _ )  ___  | _ ) ___ _ __ | |__  "
t4 = " | _ \ |___| | _ \/ _ \ '  \| '_ \ "
t5 = " |___/       |___/\___/_|_|_|_.__/ "
t6 = "                                   "
t7 = "    [*] Browser Bomb By JackCDK    "
ta = "              [V1.0.1]             "
t8 = "==================================="
t9 =""

print(Fore.CYAN + t1)
print(Fore.WHITE + t2)
print(Fore.WHITE + t3)
print(Fore.WHITE + t4)
print(Fore.WHITE + t5)
print(Fore.WHITE + t6)
print(Fore.WHITE + t7)
print(Fore.WHITE + ta)
print(Fore.CYAN + t8)
print(Fore.WHITE + t9)

#dashd = raw_input("[?] what sort of http does the site use?:")

websi = raw_input("[?] What site do you want to use?:")

snum = int(input("[?] How many times do you want to spam your pc?: "))

for word in ['spaming'] * snum:
    webbrowser.open(hlink+websi)
    time.sleep(0.9)