import requests

url = 'https://yandex.ru/maps/-/CGWdv8id'

response = requests.get(url)
text = response.text
print(text)