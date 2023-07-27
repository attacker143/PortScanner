import socket
import threading
import time

print_lock = threading.Lock()
   
host =input("domain name : ")
ip=socket.gethostbyname(host)

print("_"*60)
print(f"Scanning Start Target IP : {ip}")
print("_"*60)


def port_scanner(port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(1)
    result = soc.connect_ex((ip, port))

    if not result:
       try:
          serviceName = socket.getservbyport(port, "tcp")
          print(f" Open	{port}	{serviceName}")

       except:
             print(f" Open	{port}	Unknow ")
             soc.close()


for port in range(1,65535+1):
    th=threading.Thread(target=port_scanner,args=(port,))
    th.start()
    
