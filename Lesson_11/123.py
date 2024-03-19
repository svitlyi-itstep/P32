import requests

def new_currency(user_input_currency):
    host = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1'
    url = f'{host}/currencies/{user_input_currency}.json'

    response = requests.get(url)

    if response.ok:
        as_json = response.json()
        if user_input_currency in as_json:
            for cur, rate in as_json[user_input_currency].items():
                print(f"1 гривня {user_input_currency} = {rate} {cur}")
            return as_json
        else:
            print("Такої валюти не має")
    else:
        print(f"{response.status_code=}")
    return None

def all_currency(user_input_currency):
    if user_input_currency == "all" or user_input_currency == "всі валюти":
        host = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"
        response = requests.get(host)
        if response.ok:
            return response.json()
        else:
            return {}

def function_convert_currency(user_input_currency, as_json):
    host = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"
    if user_input_currency == "конвертувати" or user_input_currency == "convert":
        input_user_currency_one = input("Введіть валюту, яку треба конвертувати: ")
        input_user_currency_two = input("Введіть валюту, в яку треба конвертувати попередню: ")

        rate_one = as_json[input_user_currency_one][input_user_currency_two]
        rate_two = as_json[input_user_currency_two][input_user_currency_one]

        amount = float(input(f"Введіть суму у {input_user_currency_one}, яку ви хочете конвертувати: "))

        converted_amount = amount * rate_one
        print(f"{amount} {input_user_currency_one} = {converted_amount} {input_user_currency_two}")

def function_examination_currency(user_input_currency):
    return user_input_currency

user_input_currency = input("введіть валюту на яку ви хочете змінити або ввести? : ")
validated_currency = function_examination_currency(user_input_currency)
as_json = new_currency(validated_currency)
if as_json:
    function_convert_currency(user_input_currency, as_json)
