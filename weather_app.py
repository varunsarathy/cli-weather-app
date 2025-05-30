import argparse
import pyfiglet
import requests
from simple_chalk import chalk

# API key for openweathermap API
API_KEY = "f9c3aa4c9f91276c43fa9216245c27cf"

# Base URL for openweathermap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Map the weather codes to weather icons
WEATHER_ICONS = {
    # Day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    
    # Night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

# Contruct API URL with query params
parser = argparse.ArgumentParser(description="Check the weather for a particular location")
parser.add_argument("country", help="The country, town or city to check the weather for")
args = parser.parse_args()

url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

# Make API request and parse response using requests module
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather info"))
    exit()
    
# Parsing JSON response from API and extracting weather info
data = response.json()

# Get info from response
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct output with weather icons
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}\n"
output += f"Feels like: {feels_like}°C\n"

# Output
print(chalk.green(output))

