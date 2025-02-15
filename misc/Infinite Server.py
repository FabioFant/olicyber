import requests
from bs4 import BeautifulSoup

s = requests.Session()
url  = 'http://infinite.challs.olicyber.it/'
r = s.get(url=url)

i = 0
while True:
    i += 1
    
    soup = BeautifulSoup(r.text, 'html.parser')
    h2 = soup.find('h2')

    if h2.text == "MATH TEST":
        print("math")
        p = soup.find('p')

        n1 = -69
        n2 = -69
        for sos in p.text.split(' '):
            if sos[0].isdigit():
                if n1 == -69:
                    n1 = int(sos)
                else:
                    n2 = int(sos[:-1])
                    break
        
        sum = n1 + n2
        r = s.post(data={'sum': str(sum)}, url=url)

    elif h2.text == "ART TEST":
        print("art")
        p = soup.find('p')

        testo = p.text.split(' ')
        col = testo[len(testo) - 1][:-1]
        r = s.post(data={col: ''}, url=url)

    elif h2.text == "GRAMMAR TEST":
        print("grammar")
        p = soup.find('p')

        testo = p.text.split(' ')
        let = testo[1][1:-1]
        par = testo[len(testo) - 1][1:-2]
        r = s.post(data={'letter': str(par.count(let)), 'submit': 'Submit'}, url=url)

    else:
        print(r.text)
        break
