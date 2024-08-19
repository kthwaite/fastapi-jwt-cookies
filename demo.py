import requests

r = requests.post(
    "http://localhost:8000/auth/token",
    data={"username": "jeff", "password": "secret"},
)
if r.status_code != 200:
    raise Exception(r.text)
print("Got cookies: %s" % r.cookies)

r = requests.get("http://localhost:8000/", cookies=r.cookies)
if r.status_code != 200:
    raise Exception(r.text)
print(r.json())
