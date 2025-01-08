# Weather-Plan

# library for converting to long/lat
pip install geopy

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Weather Plan")
userloc = input("Enter your destination: ") 

location = geolocator.geocode(userloc)
print(location.address)
latitude = location.latitude
longitude = location.longitude
print((latitude, longitude))

!pip install requests
import requests

# get weather forecast from NWS
def nws(lat,long):
  url = f"https://api.weather.gov/points/{lat},{long}"
  response = requests.get(url)
  data = response.json()
  forecast_url = data['properties']['forecastHourly']
  return forecast_url
def get_forecast(forecast_url):
  response = requests.get(forecast_url)
  forecast_data = response.json()
  return forecast_data

# clothing_rec
def generate_clothing_recommendations(weather_data):
    openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key
    forecast = weather_data["forecast"]["forecastHourly"]
    temp = forecast["avgtemp_f"]
    rain = forecast["daily_chance_of_rain"]
    wind = forecast["maxwind_mph"]
    prompt = f"""Based on the following weather data:
    - Average Temperature: {temp}°F
    - Chance of Rain: {rain}%
    - Wind Speed: {wind} mph
    Suggest appropriate clothing for the day."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
