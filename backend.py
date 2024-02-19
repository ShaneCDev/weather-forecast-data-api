import requests

API_KEY = '0ab7922ce48d17f46cb7314eb75bf37b'


def get_data(place, forecast_days, type):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    num_value = 8 * forecast_days
    filtered_data = filtered_data[:num_value]
    if type == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if type == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place="Tokyo", forecast_days=3, type="Temperature"))
