import requests
import json

class OpenMapAI:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name):

        url = f"{self.base_url}q={city_name}&appid={self.api_key}"
        response = requests.get(url)
        #Error Check
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Check city Name, Network Connection, or API services is down.")
            return