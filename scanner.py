import subprocess

Up = []
Down = []

def ping(ip,i):
    ping_test = subprocess.call(f'ping {ip[0]}.{i}')
    if ping_test == 0:
       #print (f'ping {ip[0]}.{i} is Up' )
       Up.append(f'{ip[0]}.{i}')
    else:
       #print (f'ping {ip[0]}.{i} is down')
       Down.append(f'{ip[0]}.{i}')

def Entire_network(ip):
    ip = ip.rsplit(".",1)
    for i in range(1,256):
        #ping = os.popen(f'ping 192.168.0.{i}').read()
        ping(ip,i)

def main():       
    ip = input("Enter the Network: ")
    Entire_network(ip)
    print ("Working Host: ",Up)
    print ("Down Host : ",Down)

if __name__ == '__main__':
    main()