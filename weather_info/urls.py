from django.urls import path
from .views import health_check, get_weather_info

urlpatterns = [
    path('ping', health_check, name="heath_check"),
    path('info', get_weather_info, name="get_weather_info")
]
