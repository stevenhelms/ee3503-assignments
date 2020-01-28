'''
This project involves gathering data from a website, parsing the data and printing out the results.
•	Use the Python requests library and retrieve weather data from the following URL. http://api.openweathermap.org/data/2.5/forecast?id=3582677&APPID=8fc532fa1fa981e1237c5ce9ed510080&units=imperial
•	Output must print:
  o	Location and country
  o	Current conditions -current temperature, current feels like temperature, weather (clear, cloudy, etc).
•	Additionally, output should contain a summary of the forecast for each day. Search through the data finding the minimum temp_min and maximum temp_max for each day. Present the results similar to below:
  o	2020-01-29 – High 80.28, Low 79.43, Clear
  o	2020-01-30 – High 82.99, Low 79.21, Light Rain
•	The weather description (i.e. clear, cloudy) should be capitalized using the .title() method on the string.
'''
