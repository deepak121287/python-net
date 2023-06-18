import paramiko
import time
from getpass import getpass


username = input('enter the username:')
password = input('enter the password:')

for csrv in range(200,202):
    ip = '192.168.145.' + str(csrv)
    print('######connecting to the device ' + ip + ' ######\n')
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(ip,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    device_access = session.invoke_shell()
    device_access.send(b'conf t\n')
    for N in range(1,2):
        device_access.send('no int lo ' +str(N) +'\n')
    #    device_access.send('int lo ' +str(N) +'\n')
    #    device_access.send('ip add 1.1.1.' +str(N) +' 255.255.255.255\n')
    time.sleep(5)
    device_access.send(b'do term length 0\n')
    device_access.send(b'do show ip int brief\n')
    time.sleep(2)
    output = device_access.recv(65000)
    print(output.decode('ascii'))
