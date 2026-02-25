import requests
from bs4 import BeautifulSoup

def has_flag(tag):
    return 'flag{' in tag.text

url1 = "http://web-16.challs.olicyber.it"
s = requests.Session()
visited_pages = []
pages = []
found = False

pages.append(url1)
while bool(pages): # not empty

    # visit url
    url = pages.pop(0)
    if url in visited_pages:
        continue
    visited_pages.append(url)

    r = s.get(url=url)
    soup = BeautifulSoup(r.text, 'html.parser')

    #check for tags h1 with flag
    h1s = soup.find_all('h1', string=has_flag)
    if h1s:
        for h1 in h1s:
            print(h1)
            found = True
            break
    if found:
        break

    # search other pages
    anchors = soup.find_all('a')
    for a in anchors:
        href = a.attrs.get('href')
        if not href:
            continue
        pages.append(url1+href)



