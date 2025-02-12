import os
#from secret import FLAG

def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

FLAG = bytes.fromhex("27893459dc8772d66261ff8633ba1e5097c10fba257293872fd2664690e975d2015fc4fd3c") # 37
car = 0
while car <= 255:
    key = b'A\xe5U>\xa7' + os.urandom(1) # xor(FLAG[:5], b'flag{') + os.urandom(1)
    print(xor(FLAG, key * (len(FLAG)//len(key) + 1)))
    car += 1
    
