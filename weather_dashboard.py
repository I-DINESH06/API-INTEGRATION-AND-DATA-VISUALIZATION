import requests
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuration ---
API_KEY = 'baca0e8e22b3d301f6db96c7664c410c'  
CITIES = ['London', 'New York', 'Tokyo', 'Chennai', 'Berlin', 'Paris']
URL = 'http://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'

# --- Data Fetching ---
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': UNITS
    }
    response = requests.get(URL, params=params)
    data = response.json()
    if response.status_code == 200:
        return {
            'City': city,
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Weather': data['weather'][0]['main']
        }
    else:
        print(f"Error fetching data for {city}: {data.get('message')}")
        return None

weather_data = [fetch_weather(city) for city in CITIES]
weather_data = [d for d in weather_data if d is not None]

# --- Visualization ---
cities = [d['City'] for d in weather_data]
temps = [d['Temperature (°C)'] for d in weather_data]
humidity = [d['Humidity (%)'] for d in weather_data]

sns.set(style="whitegrid")
plt.figure(figsize=(16, 10))

# Temperature Bar Plot
plt.subplot(2, 2, 1)
sns.barplot(x=temps, y=cities, palette='coolwarm')
plt.title("Temperature by City")
plt.xlabel("Temperature (°C)")

# Humidity Bar Plot
plt.subplot(2, 2, 2)
sns.barplot(x=humidity, y=cities, palette='Blues_d')
plt.title("Humidity by City")
plt.xlabel("Humidity (%)")

# Scatter Plot: Temperature vs Humidity
plt.subplot(2, 1, 2)
sns.scatterplot(x=temps, y=humidity, hue=cities, s=100)
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")

plt.tight_layout()
plt.show()
