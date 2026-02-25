import requests
from bs4 import BeautifulSoup
from bs4 import Comment

def isComment(tag):
    return(isinstance(tag, Comment))

url1 = "http://web-14.challs.olicyber.it/"

s = requests.Session()
r = s.get(url=url1)

soup = BeautifulSoup(r.text, 'html.parser')
comments = soup.find_all(string=isComment)

for c in comments:
    print(c, end="")




