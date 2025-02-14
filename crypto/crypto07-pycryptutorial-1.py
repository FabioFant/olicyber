from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Cipher import ChaCha20
from Crypto.Util.Padding import pad
from Crypto.Util.number import *

if(True):
    key = bytes.fromhex('c5a86443c6abd4ec')
    cipher = DES.new(key=key, mode=DES.MODE_CBC)
    messaggio = 'La lunghezza di questa frase non è divisibile per 8'
    plaintext = pad(messaggio.encode(), 8, style='x923')

    encrypted = cipher.encrypt(plaintext)
    print(hex(bytes_to_long(encrypted)))

    civ = cipher.iv
    print(hex(bytes_to_long(civ)))

    print('-----------------------------------------------')

#--------------------------------------------------------------------

if(True):
    k = 'a' * 64
    key = bytes.fromhex(k)
    print(k)

    cipher = AES.new(key=key , mode=AES.MODE_CFB, segment_size=24)
    messaggio = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
    plaintext = pad(messaggio.encode(), 16, style='pkcs7')

    encrypted = cipher.encrypt(plaintext)
    print(hex(bytes_to_long(encrypted)))

    civ = cipher.iv
    print(hex(bytes_to_long(civ)))

    print('-----------------------------------------------')

#--------------------------------------------------------------------

if(True):
    key = bytes.fromhex('3097530ce81eb5a3b67eb712b7324d22ce0131eda25628510aa3b64186a659da')
    nonce = bytes.fromhex('dec04d359c35446d')

    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = bytes.fromhex('5d852358036d916fa332087d03793caf25d53844d92eda8487a47d24')

    decrypted = cipher.decrypt(ciphertext)
    print(decrypted)

    print('-----------------------------------------------')
