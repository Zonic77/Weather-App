import requests

print("Welcome to my weather app!")

api_key = "c118b03e449b505a5ca490063354dab7"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Please enter the name of the city: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
weather_data = response.json()

main = weather_data["main"]

temp = main["temp"]
temperature = (1.8*(temp-273) + 32)
humidity = main["humidity"]

weather = weather_data["weather"]

weather_description = weather[0]["description"]

print(" Temperature (in Fahrenheit unit) = " +
                str(temperature) +
      "\n humidity = " +
                str(humidity) +
      "\n description = " +
                str(weather_description))
 
input('Press ENTER to exit')