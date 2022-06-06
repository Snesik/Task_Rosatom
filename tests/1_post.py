import requests
import uuid

print(str(uuid.uuid4()))
url = 'http://127.0.0.1:6000/flames/'
files = [('files', open('images/1.jpeg', 'rb')),
         ('files', open('images/2.jpeg', 'rb'))]
resp = requests.post(url=url, files=files)
print(resp.json())
