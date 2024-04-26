import requests
import json

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def compare_temperatures(city1, city2):
    data_city1 = get_weather(city1)
    data_city2 = get_weather(city2)
    
    temp_city1 = data_city1['main']['temp']
    temp_city2 = data_city2['main']['temp']
    
    temp_diff = abs(temp_city1 - temp_city2)
    
    return temp_diff, temp_city1, temp_city2

def check_rain(city):
    data = get_weather(city)
    if 'rain' in data:
        return True
    else:
        return False

def main():
    city1 = 'Pune'
    city2 = 'Dubai'
    
    temp_diff, temp_city1, temp_city2 = compare_temperatures(city1, city2)
    raining_pune = check_rain(city1)
    raining_dubai = check_rain(city2)
    
    if temp_diff >= 10:
        print("The temperature difference is significant.")
    elif temp_diff >= 5:
        print("It's quite hot.")
    else:
        print("The temperature difference is manageable.")
    
    if raining_pune:
        print(f"It's raining in {city1}.")
    if raining_dubai:
        print(f"It's raining in {city2}.")
    
    print(f"Temperature in {city1}: {temp_city1}°C")
    print(f"Temperature in {city2}: {temp_city2}°C")

if __name__ == "__main__":
    main()
