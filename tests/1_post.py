import requests
import uuid


# url = 'http://127.0.0.1:6000/flames/'
# files = [('files', open('images/1.jpeg', 'rb')),
#          ('files', open('images/2.jpeg', 'rb'))]
# resp = requests.post(url=url, files=files)
# print(resp.status_code, resp.json())

url = 'http://127.0.0.1:6000/flames/2'
files = [1,2]
resp = requests.get(url=url)
print(resp.status_code, resp.json())