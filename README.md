# Weather-Plan

# library for converting to long/lat
pip install geopy

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Weather Plan")
userloc = input("Enter your location: ") 
# use: '175 5th Avenue NYC' as an example

location = geolocator.geocode(userloc)
print(location.address)
print((location.latitude, location.longitude))

!pip install requests
import requests

def nws(lat,long):
  url = f"https://api.weather.gov/points/{latitude},{longitude}"
  response = requests.get(url)
  data = response.json()
  forecast_url = data['properties']['forecastHourly']
  return forecast_url

# clothing_rec
def generate_clothing_recommendations(weather_data):
    openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key
    forecast = weather_data["forecast"]["forecastday"][0]["day"]
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
