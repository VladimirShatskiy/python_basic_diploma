import json
from typing import Any
import requests
from config_data import config


def get_city_id(city_name: str = 'minsk') -> str:
    """
    по имени города возвращает ID через API запрос
    :return: str - ID города
    """

    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q": city_name, "locale": "en_US", "langid": "1033", "siteid": "300000001"}

    headers = {
        "X-RapidAPI-Key": config.RAPID_API_KEY,
        "X-RapidAPI-Host": config.X_RapidAPI_Host
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    date = json.loads(response.text)

    return date['sr'][1]['gaiaId']


def get_hotel_in_city(id_city: str = '2427', price_max: int = 30000, price_min: int = 1,
                      check_in_date: dict = None, check_out_date: dict = None, number_hotel:
                      int = 200) -> list[dict[str, Any]]:
    """

    :param id_city: id города по его названию (из get_city_id)
    :param price_max: максимальная стоимость номера отеля для выгрузки по API
    :param price_min: минимальная стоимость номера отеля
    :param check_in_date: дата заселения в номер
    :param check_out_date: дата выезда из номера
    :param number_hotel: количество отелей для вывода в список
    :return: список словарей отелей
            {name - название отеля,
            id - id отеля,
            distance - расстояние до центра города,
            price - стоимость ноимера,
            image_main - ссылка на главный вид отеля
    """

    if check_in_date is None:
        check_in_date = {"day": 15, "month": 12, "year": 2022}
        check_out_date = {"day": 16, "month": 12, "year": 2022}

    url = "https://hotels4.p.rapidapi.com/properties/v2/list"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": id_city},
        "checkInDate": {
            "day": check_in_date['day'],
            "month": check_in_date['month'],
            "year": check_in_date['year']
        },
        "checkOutDate": {
            "day": check_out_date['day'],
            "month": check_out_date['month'],
            "year": check_out_date['year']
        },
        "rooms": [
            {
                "adults": 1,
                "children": []
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": number_hotel,
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {"price": {
            "max": price_max,
            "min": price_min
        }}
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": config.RAPID_API_KEY,
        "X-RapidAPI-Host": config.X_RapidAPI_Host
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    data = json.loads(response.text)
    list_hotels_city = []
    for i_hotel in data['data']["propertySearch"]['properties']:
        hotel = {
            "name": i_hotel['name'],
            "id": i_hotel['id'],
            "distance": i_hotel['destinationInfo']['distanceFromDestination']['value'],
            "price": i_hotel['price']['lead']['amount'],
            "image_main": i_hotel['propertyImage']['image']['url']
        }
        list_hotels_city.append(hotel)

    return list_hotels_city


def get_options_hotel(hotel: dict, max_photo: int = 5) -> dict:
    """
    запрос всех опций отеля по API
    :param hotel: словарь отеля по которому необходимо получить опции
    :param max_photo: максимальное количество ссылок на фотографии отеля
    :return: словарь отеля дополненный addres- адресом отеля и hpotos - списоком ссылко на фото отеля
    """

    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": config.RAPID_API_KEY,
        "X-RapidAPI-Host": config.X_RapidAPI_Host
    }

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotel['id']
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    data = json.loads(response.text)

    i_photo = 0
    list_photo = []
    for photos in data['data']['propertyInfo']['propertyGallery']['images']:
        list_photo.append(photos['image']['url'])
        i_photo += 1
        if i_photo >= max_photo:
            break

    hotel['address'] = data['data']['propertyInfo']['summary']['location']['address']['addressLine']
    hotel['photos'] = list_photo

    return hotel


def lower_price(number_hotels: int = 2):
    with open('file_list_3', 'r', encoding='utf-8') as file:
        hotels_list = json.load(file)

    for hotel in hotels_list[:number_hotels]:
        if not 'address' in hotel:
            print('123')
            options = get_options_hotel(hotel)
            hotel['address'] = options['address']
            hotel['photos'] = options['photos']

    with open('file_list_3', 'w', encoding='utf-8') as file:
        json.dump(hotels_list, file, indent=4)

    return hotels_list[:number_hotels]


