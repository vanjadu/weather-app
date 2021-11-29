import json
import tkinter as tk
from tkinter import font
import requests
import time


def getWeather(canvas):
    city = textfield.get()
    # Get your api key at https://openweathermap.org/api
    api_key = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
        city + '&appid={** Your api key **}'
    # Call all the data you want to display in your app
    json_data = requests.get(api_key).json()
    condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.5)
    min_temperature = int(json_data['main']['temp_min'] - 273.5)
    max_temperature = int(json_data['main']['temp_max'] - 273.5)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise_time = time.strftime('%H:%M:%M', time.gmtime(
        json_data['sys']['sunrise'] - 3600))
    sunset_time = time.strftime('%H:%M:%M', time.gmtime(
        json_data['sys']['sunset'] - 3600))

    # Combine the data you called
    final_info = condition + '\n' + str(temperature) + '°C'
    final_data = '\n' + 'Max temp: ' + \
        str(max_temperature) + '\n' + 'Min temp: ' + \
        str(min_temperature) + '\n' + 'Pressure: ' + \
        str(pressure) + '\n' + 'Humidity: ' + str(humidity) + \
        '\n' + 'Wind speed: ' + \
        str(wind_speed) + '\n' + 'Sunrise: ' + \
        sunrise_time + '\n' + 'Sunset: ' + sunset_time
    # Display the data
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry('600x500')
canvas.configure(bg='#000957')
canvas.title('Vanja\'s Weather App')

f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')

textfield = tk.Entry(canvas, font=t, bg='#fff', fg='#9A0680')
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t, fg='#577BC1', bg='#000957')
label1.pack()

label2 = tk.Label(canvas, font=f, fg='#344CB7', bg='#000957')
label2.pack()

canvas.mainloop()
