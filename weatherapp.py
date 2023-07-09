import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "d695fc375e8e5abc0f05dbc73b34d34d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather(api_key, city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != "404":
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        messagebox.showinfo("Weather Info", f"Weather in {city}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {description}")
    else:
        messagebox.showerror("Error", "City not found.")

def get_forecast(api_key, city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(FORECAST_URL, params=params)
    data = response.json()

    if data["cod"] != "404":
        forecast_text = f"Weather forecast for {city}:\n"
        for forecast in data["list"]:
            date = forecast["dt_txt"]
            temperature = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            forecast_text += f"\nDate: {date}\nTemperature: {temperature}°C\nDescription: {description}\n"
        messagebox.showinfo("Forecast", forecast_text)
    else:
        messagebox.showerror("Error", "City not found.")

def save_favorite(city):
    with open("favorites.txt", "a") as file:
        file.write(city + "\n")
    messagebox.showinfo("Favorite Saved", f"{city} added to favorites.")

def view_favorites():
    try:
        with open("favorites.txt", "r") as file:
            favorites = file.readlines()
            if not favorites:
                messagebox.showinfo("Favorites", "No favorite locations saved.")
            else:
                favorites_text = "Favorite locations:\n"
                for index, city in enumerate(favorites, start=1):
                    favorites_text += f"{index}. {city.strip()}\n"
                messagebox.showinfo("Favorites", favorites_text)
    except FileNotFoundError:
        messagebox.showinfo("Favorites", "No favorite locations saved.")

def show_weather():
    city = entry.get()
    if city:
        get_weather(API_KEY, city)
    else:
        messagebox.showerror("Error", "Please enter a city name.")

def show_forecast():
    city = entry.get()
    if city:
        get_forecast(API_KEY, city)
    else:
        messagebox.showerror("Error", "Please enter a city name.")

def save_favorite_location():
    city = entry.get()
    if city:
        save_favorite(city)
    else:
        messagebox.showerror("Error", "Please enter a city name.")
#create title
root = tk.Tk()
root.title("Weather App")

#create label city
label = tk.Label(root, text="Enter city name:")
label.pack(pady=10)

entry = tk.Entry(root, font=("formal script", 14))
entry.pack(pady=5)

#create button for current weather
weather_button = tk.Button(root, text="Get Current Weather", command=show_weather)
weather_button.pack(pady=5)

#create button for forecast weather
forecast_button = tk.Button(root, text="Get Weather Forecast", command=show_forecast)
forecast_button.pack(pady=5)

# create a button for favorite location
favorite_button = tk.Button(root, text="Save Favorite Location", command=save_favorite_location)
favorite_button.pack(pady=5)

#create a button for view favorite location  
favorites_button = tk.Button(root, text="View Favorite Locations", command=view_favorites)
favorites_button.pack(pady=5)

root.mainloop()
