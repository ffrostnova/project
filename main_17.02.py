from request_sender import get_all_currencies, converter

ALL_CURRENCIES = get_all_currencies()

print("Добро пожаловать, уважаемый клиент!")

print("""
Наша программа поможет Вам конвертировать вашу валюту:
- Выберите валюту, которую хотите перевести;
- Вводите количество этой валюты;
- Выберите валюту для конвертации

""")

counter = 1
for i in ALL_CURRENCIES:
    print(f"{counter} -> {i}")
    counter += 1

current_value = input('Введите имеющуюся валюту: ').upper()

count_of_current_value = float(input('Введите количество имеющейся валюты: '))

conversion_currency = input("Выберите валюту для конвертации: ").upper()

conversion_result = converter(conversion_currency, current_value) * count_of_current_value

print(f'Ваша сумма составила {round(conversion_result, 2)} {conversion_currency}')