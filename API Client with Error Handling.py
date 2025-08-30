# Weather API client with comprehensive error handling
import requests
import json
from datetime import datetime

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def get_weather(self, city):
        try:
            url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'timestamp': datetime.fromtimestamp(data['dt'])
            }
            
            return weather_info
            
        except requests.exceptions.RequestException as e:
            return f"Network error: {e}"
        except KeyError as e:
            return f"Unexpected API response format: {e}"
        except json.JSONDecodeError:
            return "Invalid JSON response"

# Usage
api = WeatherAPI('your_api_key_here')
result = api.get_weather('London')
print(result)
