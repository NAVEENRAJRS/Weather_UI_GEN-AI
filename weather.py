import requests

API_KEY = "ee75b683f2a94a67359984fbe5bfa28b"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()

    return None