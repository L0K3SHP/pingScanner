import subprocess
import re
#import os  

Up = []
Down = []

def check(a):
    chk = re.findall("[a-z,A-Z]",a)
    if len(chk) == 0:
        exit
    elif len(chk) >0:
        print("\n\n\n Enter the Network wanted to sacn the hosts")
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
       Down.append(f'{i}')


def Particular_network(ip_list):
    for i in ip_list:
        #ping = os.popen(f'ping 192.168.0.{i}').read()
        ping_sg(i)

def Entire_network(ip,strt,enD):
    ip = ip.rsplit(".",1)
    for i in range(strt,enD+1):                #testing range
        #ping = os.popen(f'ping 192.168.0.{i}').read()
        ping(ip,i)

def main():       
    op = int(input("Choose the operation \n1.Particular Ip\'s \n2.Entire Network \nChoose your Operation: \t\t"))
    if op == 1:
        ip_list = []
        ip_list1 = input("Enter the Ip's/doamin seprated by comma(,): ")
        ip_list1 = ip_list1.split(',')
        ip_list.append(ip_list1)
        Particular_network(ip_list1)  
    elif op == 2:
        ip = input("Enter the Network: ")
        check(ip)
        op1 = int(input("Choose the opertaion \n1:Default(Entire Network)  \n2:Custome Range  \nChoose your Operation: \t\t"))
        if op1 == 1:
            strt = 1
            enD = 255
            Entire_network(ip,strt,enD)
        elif op1 == 2: 
            print("Enter the range\n")
            strt = int(input("Enter the Starting host:"))
            enD = int(input("Enter the Ending host:"))
            Entire_network(ip,strt,enD)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print ("Working Host: ",Up)
        print ("Down Host : ",Down)
