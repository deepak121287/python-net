import getpass
import telnetlib

HOST = "192.168.145.200"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"sh ip int brief\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))