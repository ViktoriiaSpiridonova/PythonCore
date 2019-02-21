import pyowm

location = input("Input city name: ")
owm = pyowm.OWM("b1dece6c34f2db7dc695d959cc187f1f")

observation = owm.weather_at_place(location)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']
print("In " + str(location) + " the temperature is " + " " + str(temperature) + " in Celsius")

print(w)
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
