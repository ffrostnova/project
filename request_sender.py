import requests


API_TOKEN = "fca_live_mL8LwHPBU8Drw0owNOGZ5oIC7TzxEW4nJvrex0xl"


def converter(currencies, base_currency):
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_TOKEN}&currencies={currencies}&base_currency={base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        value = data['data'][currencies]
        print(f"Стоимость {base_currency} равняется {value} {currencies}")
        return value

    else:
        print('Безуспешный запрос')


def get_all_currencies():
    url = f"https://api.freecurrencyapi.com/v1/currencies?apikey={API_TOKEN}&currencies=&base_currency="
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        all_currencies = data['data']
        all_values = all_currencies.keys()
        result = list(all_values)
        return result
    else:
        print('Безуспешный запрос')
