import requests

url = "https://usecase2-agent.azurewebsites.net:8000"

x = requests.get(url + '/user', timeout=15)
print(x.text)