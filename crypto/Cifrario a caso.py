import random

def decrypt(enc):
    byt = bytes.fromhex(enc)

    for i in range(0, 256):
        plaintext = []
        random.seed(i)

        for b in byt:
            decrypted_char = b ^ random.randint(0, 255)
            plaintext.append(decrypted_char)
        
        print(bytes(plaintext))

decrypt("088596df93697e62d71cb143352ccb45be15463219c6cc917f9be83c1aa1f7d0217b4586c1058009")

