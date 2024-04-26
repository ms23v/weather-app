# Python Weather App

This Python weather app fetches current weather data for two cities, Pune and Dubai, using the OpenWeatherMap API. It compares the temperatures between these cities and displays messages based on the temperature difference, along with checking if it's raining in either city.

## How to Use

1. Get an API Key from OpenWeatherMap:
   - Sign up or log in to OpenWeatherMap (https://home.openweathermap.org/users/sign_up).
   - Navigate to your API keys section and copy your API key.

2. Install Required Libraries:
   ```bash
   pip install requests
3. Replace YOUR_API_KEY:
In the get_weather function, replace YOUR_API_KEY with your actual API key obtained from OpenWeatherMap.
4. Run the App:
Open a terminal.
Navigate to the directory containing the weather_app.py file.
Run the following command:

python main.py

## Features

Fetches current weather data using the OpenWeatherMap API.
Compares temperatures between Pune and Dubai.
Displays messages based on the temperature difference:
"The temperature difference is significant."
"It's quite hot."
"The temperature difference is manageable."
Checks if it's raining in Pune and/or Dubai.
Prints the temperatures in Celsius for Pune and Dubai.

##Dependencies

Python 3.x
requests library for making HTTP requests (install using pip install requests)

Example Output:
The temperature difference is significant.
It's raining in Pune.
Temperature in Pune: 30°C
Temperature in Dubai: 40°C
