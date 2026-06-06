import requests

API_KEY = "d08286c7afeb389906cbd3c66b1397a4"
city = input("Enter a city to check: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

response = requests.get(url)
data = response.json()

temp = data["main"]["temp"]
weather = data["weather"][0]["description"]
wind = data["wind"]["speed"]

print(f"n--- Weather Report for {city} ---")
print(f"Temperature: {temp}°F")
print(f"conditions: {weather}")
print(f"Wind Speed: {wind} mph")

print("\n--- Network Alert Status ---")

if wind > 40:
    print("⚠️ ALERT: High winds may cause network disruptions!")
elif temp < 15:
    print("⚠️ ALERT: Extreme cold may affect network equipment!")
elif "storm" in weather or "thunder" in weather:
    print("⚠️ ALERT: Storm conditions detected - outage risk high!")
else:
    print("✅ All clear - No network disruptions expected.")

while True:
    city = input("Enter a city to check (or 'quit' to exit): ")
    if city.lower() == "quit":
        print("Goodbye!")
        break
    check_city(city) # type: ignore

