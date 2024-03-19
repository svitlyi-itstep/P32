import requests

def get_currencies():
    url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return {}

def get_rate(currency_from, currency_to):
    host = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1'
    url = f'{host}/currencies/{currency_from}.json'
    response = requests.get(url)

    if response.ok:
        return response.json()[currency_from][currency_to]
    else:
        return 0


currencies_list = get_currencies()
currency_from = 'eur'
currency_to = 'uah'
amount = 20
rate = get_rate(currency_from, currency_to)

print(f'1 {currencies_list[currency_from]} = {round(rate, 2)} {currency_to}')


'''
    1. Зробити так, що користувач вводив яку валюту треба поміняти, на яку і скільки
    2. Перевіряти введені валюти на коректність
    3. Замість скорочених кодів валют при виведенні використовувати повні назви
'''

