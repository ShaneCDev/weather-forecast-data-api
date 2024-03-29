import requests
import os

API_KEY = os.environ.get('API_KEY')


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    num_value = 8 * forecast_days
    filtered_data = filtered_data[:num_value]
    return filtered_data

