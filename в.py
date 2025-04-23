# Первое задание
import requests

# API-ключ от OpenWeatherMap
API_KEY = "ae707a3b62fe7fc9361f1dab8439b415"

# Ввод города
print("Введите нужный вам город для просмотра погоды")
CITY_NAME = input()

# URL для запроса
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric&lang=ru"

# GET-запрос
response = requests.get(url)

# Проверка запроса
if response.status_code == 200:
    # Парсим JSON-ответ
    data = response.json()

    # Извлекаем нужные данные
    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather_description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    # Вывод информации
    print(f"Погода в городе {city}:")
    print(f"Температура: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Описание: {weather_description.capitalize()}")
    print(f"Скорость ветра: {wind_speed} м/с")
else:
    print(f"Ошибка при запросе: {response.status_code}")



# Второе задание
import requests

# API-ключ от dictionaryapi.com
API_KEY = "f8314422-8ea1-4c84-8177-6a980cdf2457"

# Ввод слова
print("Введите желаемое слова на английском языке для того чтобы увидеть его: часть речи, определение, синонимы, антонимы")
WORD = input()

# URL для запроса
url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{WORD}?key={API_KEY}"

# Выполняем GET-запрос
response = requests.get(url)

# Проверяем, что запрос успешен
if response.status_code == 200:
    # Парсим JSON-ответ
    data = response.json()

    # Проверка запоса
    if data and isinstance(data, list) and isinstance(data[0], dict):
        # Извлекаем первую запись
        first_entry = data[0]

        # Извлекаем нужные данные
        word = first_entry.get("meta", {}).get("id", "N/A")
        part_of_speech = first_entry.get("fl", "N/A")
        definition = first_entry.get("shortdef", ["N/A"])[0]

        # Извлекаем синонимы и антонимы
        synonyms = first_entry.get("meta", {}).get("syns", [["N/A"]])[0]
        antonyms = first_entry.get("meta", {}).get("ants", [["N/A"]])[0]

        # Выводим информацию
        print(f"Слово: {word}")
        print(f"Часть речи: {part_of_speech}")
        print(f"Определение: {definition}")
        print(f"Синонимы: {', '.join(synonyms)}")
        print(f"Антонимы: {', '.join(antonyms)}")
    else:
        print(f"Слово '{WORD}' не найдено в словаре.")
else:
    print(f"Ошибка при запросе: {response.status_code}")