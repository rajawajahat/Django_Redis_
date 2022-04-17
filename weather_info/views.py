from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from .cache import Cache
from .utils import get_last_observation, get_temperature, get_wind
import requests, json


def health_check(request):
    return JsonResponse({'data': 'pong'})


def get_weather_info(request):
    response = {}

    scode = request.GET.get("scode")
    if not scode:
        return HttpResponseBadRequest("scode parameter is required!")

    no_cache = request.GET.get("nocache")
    if not no_cache and not no_cache == 1:
        cached_value = Cache().get_key(scode)
        if cached_value:
            return JsonResponse({'data': json.loads(cached_value)})

    url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{scode}.TXT"

    rep = requests.get(url)
    if rep.status_code == 200:
        json_data = rep.text.split(" ")
        print(f"json_data: {json_data}")
    else:
        return HttpResponseServerError("verify if you have entered the correct scode!")

    response["station"] = scode
    response["last_observation"] = get_last_observation(json_data)
    response["temperature"] = get_temperature(json_data)
    response["wind"] = get_wind(json_data)

    Cache().set_key(scode, json.dumps(response))
    return JsonResponse({'data': response})
