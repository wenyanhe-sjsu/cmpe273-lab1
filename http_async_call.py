import requests
import threading

def call_url(url):
    r = requests.get(url)
    print(r.headers['date'])

url = 'https://webhook.site/bc217c92-0bd2-4888-aaac-e7a42f2ae937'

for i in range(3):
    t = threading.Thread(target=call_url, args=(url,))
    t.start()
