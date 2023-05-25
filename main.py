import urllib.request

opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())


import requests

response = requests.get("https://coinmarketcap.com/get")
print(response.text)
response_parse = response.text.split('<span>')
for elem in response_parse:
    if elem.startswith('$'):
        print(elem)