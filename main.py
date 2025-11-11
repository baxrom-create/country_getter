#sdfsdfkusdhgfhjgsdhjfgsdfhs
import requests

while True:
    country = input("Введите страну: ")
    if not country:
        break

    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Ошибка запроса или страна не найдена.")
        continue

    data = response.json()
    if isinstance(data, list):
        info = data[0]

        name = info["name"]["common"]
        capital = info.get("capital", ["Нет данных"])[0]
        currencies = list(info.get("currencies", {}).keys())
        languages = list(info.get("languages", {}).values())
        population = info.get("population", "Нет данных")
        area = info.get("area", "Нет данных")

        print(f"Страна: {name}")
        print(f"Столица: {capital}")
        print(f"Валюты: {currencies}")
        print(f"Языки: {languages}")
        print(f"Численность населения: {population}")
        print(f"Площадь: {area}")
    else:
        print("Страна не найдена.")
