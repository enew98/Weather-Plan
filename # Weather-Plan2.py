# Weather-Plan

# imports
from geopy.geocoders import Nominatim  
import requests
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variable
openai_api_key = os.getenv("OPEN_AI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key

# Converting user input to latitude & longitude coordinates
geolocator = Nominatim(user_agent="Weather Plan")
userdest = input("Enter your destination: ") 
destination = geolocator.geocode(userdest)

# Retrieving weather forecast from NWS
def nws(lat, long):
    url = f"https://api.weather.gov/points/{lat},{long}"
    response = requests.get(url)
    data = response.json()
    forecast_url = data['properties']['forecastHourly']
    return forecast_url

def get_forecast(forecast_url):
    response = requests.get(forecast_url)
    forecast_data = response.json()
    return forecast_data

# ChatGPT recommends clothing
def generate_clothing_recommendations(forecast_data):
    forecast = forecast_data["properties"]["periods"][0] # get the first hourly forecast 
    temp = forecast["temperature"]
    rain = forecast["probabilityOfPrecipitation"]
    wind = forecast["windSpeed"]
    
    prompt = f"""Based on the following weather data:
    - Average Temperature: {temp}°F
    - Chance of Rain: {rain}%
    - Wind Speed: {wind} mph
    Suggest appropriate clothing for the day."""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message['content'].strip()

# Get latitude and longitude
latitude = destination.latitude
longitude = destination.longitude

# Retrieve weather forecast and generate recommendations
forecast_url = nws(latitude, longitude)
forecast_data = get_forecast(forecast_url)
recommendation = generate_clothing_recommendations(forecast_data)

# Print recommendation
print(recommendation)