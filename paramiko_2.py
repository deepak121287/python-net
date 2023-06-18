import paramiko
import time
from getpass import getpass

ip = input('enter the ip:')
username = input('enter the username:')
password = input('enter the password:')

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

device_access = session.invoke_shell()
device_access.send(b'conf t\n')
for N in range(1,5):
    device_access.send('no int lo ' +str(N) +'\n')
#    device_access.send('ip add 1.1.1.' +str(N) +' 255.255.255.255\n')
time.sleep(5)
device_access.send(b'do term length 0\n')
device_access.send(b'do show ip int brief\n')
time.sleep(2)
output = device_access.recv(65000)
print(output.decode('ascii'))

session.close()