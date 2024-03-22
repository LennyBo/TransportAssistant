import urequests
import ujson
import time
import timeService
from secret import LAT
from secret import LON
from secret import API_KEY

UTC_OFFSET = 2 * 60 * 60

def apiWeather():
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"
    response = urequests.get(url)
    if(response.status_code == 200):
        weather_data = ujson.loads(response.text)
        return processJson(weather_data)
    else:
        print("Error occurred while retrieving weather data:", response.status_code)


def processJson(data):
    print('Processing Data...')
    # Extract the datetime and ID from each forecast and add them to the dictionary
    weather_dict = {}
    year, month, dayOfMonthToday, hour, minute, second, weekday, yearday = time.gmtime(timeService.tEpoch)
    for forecast in data['list']:
        dt = forecast['dt']
        year, month, mday, hour, minute, second, weekday, yearday = time.gmtime(dt)
        weather_id = forecast['weather'][0]['id']
        condition_description = forecast['weather'][0]['description']
        temp = round(forecast['main']['temp'] - 273.15)
        # Check if the forecast time is within the desired range
        if (hour == 6 and mday == dayOfMonthToday) or (hour == 18 and mday == dayOfMonthToday):
            weather_dict[dt] = (weather_id, condition_description,temp)
            
    return weather_dict


def shouldTakeBike(w):
    for weather in w.values():
        id,_, temp = weather
        if(((id < 700 or id >= 900) and id != 500) or temp < 13):
            print('bad weather cus', id, temp)
            return False
    print('good weather')
    return True
