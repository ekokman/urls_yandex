import csv
from typing import Tuple, List

import requests


def get_address_and_coordinates(url: str) -> Tuple[str, str, str]:
    response = requests.get(url)
    text = response.text
    list_text = text.split("address")
    for i, elem in enumerate(list_text):
        if 'coordinates' in elem and elem.startswith('":"'):
            address = elem.lstrip('":"').split("kind")[0].split('"')[0]
            coordinates = elem.split("coordinates")[1].lstrip('":[').split(']')[0]
            longitude, latitude = coordinates.split(',')
            break
    return address, latitude, longitude # адрес, широта, долгота

def writedata(urls: List[str]) -> None:
    csvData = []
    for url in urls:
        csvData.append(get_address_and_coordinates(url))

    with open('data.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=';')
        writer.writerows(csvData)
    csvFile.close()

if __name__ == '__main__':
    yandex_map_urls = [
        # 'https://yandex.ru/maps/-/CBRSVACaKB',
        # 'https://yandex.ru/maps/-/CGW-eSiw',
        # 'https://yandex.ru/maps/-/CGW-qAn7',
        # 'https://yandex.ru/maps/-/CGW-uV-S',
        # 'https://yandex.ru/maps/-/CGW-yXnh',
        'https://yandex.ru/maps/-/CGWdr2os',
        'https://yandex.ru/maps/-/CGWdvVZm',
        'https://yandex.ru/maps/-/CGWdvGk~',
        'https://yandex.ru/maps/-/CGWdv8id'

    ]
    writedata(yandex_map_urls)
