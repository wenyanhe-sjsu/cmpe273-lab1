# I am using multithreading in this little experiment.  Without use of
# synchronization tools such as mutex or semaphore, each thread is inherently
# asynchronous.

import requests
import threading

def call_url(url):  # thread function
    r = requests.get(url)
    print(r.headers['date'])

url = 'https://webhook.site/bc217c92-0bd2-4888-aaac-e7a42f2ae937'

for i in range(3):  # create three threads each of which executes the same
                    # thread function
    t = threading.Thread(target=call_url, args=(url,))
    t.start()
