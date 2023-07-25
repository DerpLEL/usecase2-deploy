import requests

url = 'http://localhost:8000'

x = requests.get(url + '/user')
print(x.text)