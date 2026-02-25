import requests

url1 = "http://web-11.challs.olicyber.it/flag_piece"
url2 = "http://web-11.challs.olicyber.it/login"
payload1 = {"username": "admin", "password": "admin"}
#cookies = {'password': 'admin'}

s = requests.Session()

for i in range(4):
    r1 = s.post(url=url2, json=payload1)
    csrf = r1.json()['csrf']
    r2 = s.get(url=url1, params={"index": i, "csrf": csrf})
    print(r2.json()['flag_piece'], end="")
    #csrf = r.json()['csrf']



