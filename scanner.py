import subprocess
import re
import os  

Up = []
Down = []


def check(a):
    chk = re.findall("[a-z,A-Z]",a)
    if len(chk) == 0:
        exit
    elif len(chk) >0:
        print("\n\n\n Enter the Network Or Ip\'s wanted to sacn the hosts")
        main()


def ping(ip,i):
    ping_test = subprocess.call(f'ping {ip[0]}.{i}',shell=False)
    if ping_test == 0:
       #print (f'ping {ip[0]}.{i} is Up' )
       Up.append(f'{ip[0]}.{i}')
    else:
       #print (f'ping {ip[0]}.{i} is down')
       Down.append(f'{ip[0]}.{i}')

def ping_sg(i):
    ping_test = subprocess.call(f'ping {i}',shell=False)
    if ping_test == 0:
       #print (f'ping{i} is Up' )
       Up.append(f'{i}')
    else:
       #print (f'ping {i} is down')
       Down.append(f'.{i}')


def Particular_network(ip_list):
    for i in ip_list:
        #ping = os.popen(f'ping 192.168.0.{i}').read()
        ping_sg(i)

def Entire_network(ip):
    ip = ip.rsplit(".",1)
    for i in range(100,110):
        #ping = os.popen(f'ping 192.168.0.{i}').read()
        ping(ip,i)

def main():       
    op = int(input("Choose the operation \n1.Particular Ip\'s \n2.Entire Network \nChoose your Operation: \t\t"))
    if op == 1:
        ip_list = ["80.50.50.06","80.80.80","192.168.0.0","ffffftfh"]
        for n in range (1,len(ip_list)+1):
            for i in ip_list:
                check(i)
                Particular_network(ip_list)  
    elif op == 2:
        ip = input("Enter the Network: ")
        check(ip)
        Entire_network(ip)
    
    print ("Working Host: ",Up)
    print ("Down Host : ",Down)

if __name__ == '__main__':
    main()