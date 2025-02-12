from pwn import *

r = remote("2048.challs.olicyber.it", 10007)
r.recvlines(2)

for i in range(2048):
    op = r.recvuntil(b' ', True)
    n1 = int(r.recvuntil(b' ', True).decode())
    n2 = int(r.recvuntil(b' ', True).decode())
    res = 0

    if op == b"SOMMA":
       res = n1 + n2
    elif op == b"DIFFERENZA":
       res = n1 - n2
    elif op == b"PRODOTTO":
        res = n1 * n2
    elif op == b"DIVISIONE_INTERA":
        res = n1 // n2
    elif op == b"POTENZA":
        res = n1 ** n2

    r.sendline(str(res).encode())
    print(i)

#print(r.recvuntil(b' ', True))
r.interactive()
