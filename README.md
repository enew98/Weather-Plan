# Weather-Plan

# library for converting to long/lat
pip install geopy
pip install requests 
import requests

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Weather Plan")
userloc = input("Enter your location: ") 
# use: '175 5th Avenue NYC' as an example

location = geolocator.geocode(userloc)
print(location.address)
print((location.latitude, location.longitude))

<!--use new long, lat for nws api -->
def nws(lat,long):
  url = f"https://api.weather.gov/points/{latitude},{longitude}"
  response = requests.get(url)
  data = response.json()
  forecast_url = data['properties']['forecastHourly']
  return forecast_url
<!-- NYC example: 40.741112, -73.989723 -->
