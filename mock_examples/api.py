from typing import Dict
import requests


def get_weather(city: str) -> Dict:
    """
    Function to get weather
    :return: Response from the API
    """
    response = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
    return response.json()
