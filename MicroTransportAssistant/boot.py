# boot.py -- run on boot-up
from wifiService import connect
import weatherApi
from notificationService import easyMessage
import timeService
from time import sleep
from machine import Pin

switchPin = Pin(2, Pin.IN)

connect()
easyMessage('Booting up')

while(True):
    secondsUntilNextAlarm = timeService.secondsUntilNextAlarm()
    print(f"Sleeping for {secondsUntilNextAlarm} seconds")
    sleep(secondsUntilNextAlarm)
    if(switchPin.value()):
        w = weatherApi.apiWeather()
        isGoodWeather = weatherApi.shouldTakeBike(w)

        if(isGoodWeather):
            easyMessage("Weather looks good")
        else:
            easyMessage("Bad weather")
    else:
        easyMessage('Switch is off')  # Todo change
