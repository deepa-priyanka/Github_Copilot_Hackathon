import requests
import json
def get_weather(city):
    api_key = '3c15e5581d88fa0f8ad5b729216d6556'
    base_url= 'http://api.openweathermap.org/data/2.5/weather?'
    url=  base_url + 'q=' + city + '&appid=' + api_key

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        # Parse the relevant weather data
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Print the weather forecast
        print(f'Weather in {city}:')
        print(f'Condition: {weather} ({description})')
        print(f'Temperature: {temperature} K')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
    else:
        print(f'Error occurred: {response.status_code} - {response.text}')

city_name=input("Enter the city name:")
get_weather(city_name)
       
