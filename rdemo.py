import requests


# r = requests.get("https://xkcd.com/353/")
# print(help(r))
# print(r.text)
# r = requests.get("https://xkcd.com/353/")

# with open('comic.png', 'wb') as f:
#     f.write(r.content)
#     f.close()

# print(r.status_code)
# print(r.ok)
payload = {
    "username": 'Nick',
    "password": "Testing"
}
# r = requests.get("http://httpbin.org/get", params=payload)
# r = requests.post("http://httpbin.org/post", data=payload)
# r = requests.get("http://httpbin.org/basic-auth/Nick/Testing", auth=('Nick', 'Testing'), timeout=3)
# r_dict = r.json()
# r = requests.get("http://httpbin.org/delay/5", auth=('Nick', 'Testing'), timeout=3)
# print(r_dict)
# print(r.text)
# print(r.url)

