import requests
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = 'fe8064ce69accf7c7e0082c6953fc686'
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 300  # Time in seconds (5 minutes)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "main": data["weather"][0]["main"],
            "temp": data["main"]["temp"] - 273.15,  # Kelvin to Celsius
            "feels_like": data["main"]["feels_like"] - 273.15,
            "dt": datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        }
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data for {city}: {e}")
        return None

weather_data = []

def collect_data():
    while True:
        for city in CITIES:
            weather = get_weather(city)
            if weather:
                weather_data.append(weather)
                print("Collected Data:", weather)
        time.sleep(INTERVAL)

def daily_summary(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['dt']).dt.date
    summary = df.groupby(['city', 'date']).agg(
        avg_temp=('temp', 'mean'),
        max_temp=('temp', 'max'),
        min_temp=('temp', 'min'),
        dominant_condition=('main', lambda x: x.mode()[0])
    ).reset_index()
    return summary

ALERT_THRESHOLD_TEMP = 35.0
alert_log = []

def check_alerts(data):
    for i in range(1, len(data)):
        if data[i]['temp'] > ALERT_THRESHOLD_TEMP and data[i - 1]['temp'] > ALERT_THRESHOLD_TEMP:
            alert_log.append(f"ALERT: High temperature in {data[i]['city']} at {data[i]['dt']} - {data[i]['temp']}°C")
            print(alert_log[-1])

def plot_temperature_trends(summary):
    for city in CITIES:
        city_data = summary[summary['city'] == city]
        plt.plot(city_data['date'], city_data['avg_temp'], label=f"{city} - Avg Temp")
        plt.plot(city_data['date'], city_data['max_temp'], linestyle="--", label=f"{city} - Max Temp")
        plt.plot(city_data['date'], city_data['min_temp'], linestyle=":", label=f"{city} - Min Temp")

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.title("Daily Temperature Trends")
    plt.show()

if __name__ == "__main__":
    collect_data()
    summary = daily_summary(weather_data)
    print("Daily Summary:")
    print(summary)
    check_alerts(weather_data)
    print("Alert Log:")
    print(alert_log)
    plot_temperature_trends(summary)
