import json
import time
import requests

from django.http import JsonResponse

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp' # Замени на URL API для получения курса доллара к рублю

last_requests = []

def get_current_usd(request):
    response = requests.get(API_URL)
    data = response.json()

    # Добавляем текущий запрос в список последних запросов
    last_requests.append(data)
    if len(last_requests) > 10:
        last_requests.pop(0)

    # Пауза между запросами
    time.sleep(10)

    return JsonResponse({
        'usd_to_rub': data,
        'last_requests': last_requests,
    })