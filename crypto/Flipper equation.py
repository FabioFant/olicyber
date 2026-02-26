from pwn import xor
from base64 import b64decode, b64encode

def xor(a,b):
  return bytes([x^y for x,y in zip(a,b)])

chipher_text = b64decode("hMhOlK/DfaNTkaibsdF4ZT0K26shQCzPvnq+/KUBewE=")

c2 = chipher_text[16:] # Can't do anything with this

c1 = chipher_text[:16]
p2 = ";pts=00000000001".encode()
px = ";pts=01000000000".encode()

# We need to modify P2 using C1 (C1 is malleable)
# N = C1 XOR P2
# P2 = N XOR C1
# P2 = C1 XOR P2 XOR C1 ----> CX
# P2 = C1 XOR P2 XOR (C1 XOR P2 XOR PX)
# P2 = PX

# CX = C1 XOR P2 XOR PX
# CX = N XOR PX

N = xor(c1, p2)
cx = xor(N, px)

flag_bytes = cx + c2
print(b64encode(flag_bytes))





