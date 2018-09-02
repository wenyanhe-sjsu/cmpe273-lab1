import requests


url = 'https://webhook.site/417464c7-cf70-42d9-b6d7-3c440e08c6cc'
for i in range(3):
    r = requests.get(url)
    print (r.headers['Date'])
