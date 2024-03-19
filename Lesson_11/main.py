import requests

url = 'https://www.whenisthenextmcufilm.com/api'

response = requests.get(url)

if response.ok:
    as_json = response.json()
    print(as_json)
    print(as_json['title'])
else:
    print(f'{response.status_code=}')


