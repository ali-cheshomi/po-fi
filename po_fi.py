from socket import *
import os
from time import sleep

# G ###########################
def serch_Motion():
    clear_terminal()
    print("searching ...")
    sleep(0.2)
    clear_terminal()
    print("Searching ..")
    sleep(0.2)
    clear_terminal()
    print("sEarching .")
    sleep(0.2)
    clear_terminal()
    print("seArching ...")
    sleep(0.2)
    clear_terminal()
    print("seaRching ..")
    sleep(0.2)
    clear_terminal()
    print("searChing .")
    sleep(0.2)
    clear_terminal()
    print("searcHing ...")
    sleep(0.2)
    clear_terminal()
    print("searchIng ..")
    sleep(0.2)
    clear_terminal()
    print("searchiNg .")
    sleep(0.2)
    clear_terminal()
    print("searchinG ...")
    sleep(0.2)
    clear_terminal()
 
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# DEF ###########################
def open_Port_Finder(ip='127.0.0.1',port=21):
 
    c_s= socket(AF_INET,SOCK_STREAM)
    c_s.settimeout(5)
    ec=0
    pg="error..."
    try:
        print('connecting ...')
        ec=c_s.connect_ex((ip,port))

        if ec==0:
            print("sucsess")
            pg = f'{port} is open'
        elif ec==10013:
            print("permission deneid") 
            pg = f'{port} is open but cant connect'   
        elif ec==10048 :
            print("already in use")
            pg = f'{port} is open'
        elif ec==10049 :
            print("can't assign requested")
            pg = f'{port} is close'
        elif ec==10054 :
            print("connection reset by peer")
            pg = f'{port} is close'
        elif ec==10060 :
            print("connection time out")
            pg = f'{port} is close'
        elif ec==10061 :
            print("connection refused")
            pg = f'{port} is close'
        elif ec==10035 :
            print("connection block")
            pg = f'{port} is open but it waiting for data to be received or sent'

        c_s.close()

    except error:
        pg = f'{port} is close'
        c_s.close()
    
    return pg

def s_Restart():
    print("Error RESTART !!!!")
    sleep(2)
    os.system('python.exe po_fi.py' if os.name == 'nt' else 'python3 po_fi.py')


# MAIN ###########################
if os.name=='nt':
    os.system('echo off')
clear_terminal()

# $values$
#$
portfindermarc="""
**
______ ___________ _____  ______ _____ _   _______ ___________ 
| ___ \  _  | ___ \_   _| |  ___|_   _| \ | |  _  \  ___| ___ \
| |_/ / | | | |_/ / | |   | |_    | | |  \| | | | | |__ | |_/ /
|  __/| | | |    /  | |   |  _|   | | | . ` | | | |  __||    / 
| |   \ \_/ / |\ \  | |   | |    _| |_| |\  | |/ /| |___| |\ \ 
\_|    \___/\_| \_| \_/   \_|    \___/\_| \_/___/ \____/\_| \_|
**                                                                                                                           
"""
pofi="""
        ______ _____ ______ _____ 
        | ___ \  _  ||  ___|_   _|
        | |_/ / | | || |_    | |  
        |  __/| | | ||  _|   | |  
        | |   \ \_/ /| |    _| |_ 
        \_|    \___/ \_|    \___/ 
                 ______           
                |______|          
port finder 
by MR_AC                          
"""
#$

_ip = '127.0.0.1'
# _ip = input("IP or WEBSITE URL > ")
_ipmin = 0
_ipmax = 0
importfiletxt = "./ips.txt"
all_ips = []
_portmin = 0
_portmax = 0
all_ports = []
_export =''
_iporfile =''
_mode = ''
_openhelpornot=''
# end $values$

# $main$
print(pofi)
_openhelpornot = input("""
countinue press => 'ENTER'
help => '-h'
\n
> """)
clear_terminal()
# end $main$

# $help$
if _openhelpornot=="-h":
    print("""
** po_fi help **
________________________

you can searching for open ports of devices or server
note> for file import mode you must create a text file and each line of the file must be an ip
    example:
          192.168.1.1
          132.1.41.45
          www.mrac.com

________________________        
""")
# end $help$




# $ip input manually or file$

_iporfile = input("IMPORT MODE => 'enter an ip' or 'read from file' (1,2) > ")

if _iporfile == '1':
    _ip = input("IP or WEBSITE URL > ")
    _ipmin = 0
    _ipmax = 1

elif _iporfile == '2':
    importfiletxt = input("enter path of ips or websites files > ")
    try:
        importfile= open(importfiletxt,'r')
    except:
        print(importfiletxt)
        print("ERORR => can't find file")
        #
        s_Restart()
    try:
        all_ips=importfile.readlines()
        print(all_ips)
        importfile.close()

    except:
        print("ERORR => can't read file")
        _ip = input("IP or WEBSITE URL > ")
        all_ips.append(_ip)
    _ipmin = 0
    _ipmax = len(all_ips)
  

else:
    print("ERORR => default mode enter a ip")
    _iporfile = '1'
    _ip = input("IP or WEBSITE URL > ")


# end $ip input manually or file$

# $mode$
_mode = input("SEARCH => 'multiple' or 'all' ports (1,2) > ")

if _mode=='1':
    print("Port Range > ")
    try:
        _portmin = int(input("(min) > "))
        _portmax = int(input("(max) > "))
    except:
        print("ERORR just enter number")
        # _portmin = 80
        # _portmax = 80
        s_Restart()

    if _portmin>_portmax:
        temp = _portmax
        _portmax = _portmin
        _portmin = temp

elif _mode=='2':
    _portmin = 0
    _portmax = 9999
else:
    print("ERORR")
    # _portmin = 80
    # _portmax = 80
    s_Restart()

# end $mode$

# $export$
_export = input("EPORT MODE => 'print on screen' or 'save to file' (1,2) > ")

if _export == '1':
    _export = '1'
elif _export == '2':
    _export = '2'
else:
    print("ERORR => default mode print on screen")
    _export = '1'
# end $export$

for ipn in range(_ipmin,_ipmax):
    if _iporfile =='2':
        _ip=all_ips[ipn]

    for i in range(_portmin,_portmax):
        try:
            serch_Motion()
            all_ports.append(open_Port_Finder(_ip,i))
        except:
            print("'ctrl + c' => esit")
            break
    if _iporfile =='2':
        _ip=all_ips[ipn]
        all_ports.append(f"{_ip} Ports :")


clear_terminal()
if _export == '1':
    print(all_ports)
elif _export == '2':
    exportfile= open("./export_Ports.txt",'w')
    for i in range(len(all_ports)):
        exportfile.write(all_ports[i])
        exportfile.write('\n')
    exportfile.close()

if os.name=='nt':
    os.system('echo on')

# END ###########################

