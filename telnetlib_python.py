from telnetlib import Telnet
cmd = input('enter the command:')
#cmd = 'sh ip int brief'
tn = Telnet('192.168.145.200')
tn.write(b'admin\n')
tn.write(b'admin@123\n')
tn.write(b'term length 0\n')
tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'exit\n')
print(tn.read_all().decode('ascii'))