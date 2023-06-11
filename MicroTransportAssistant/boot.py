from wifiService import connect
import weatherApi
from notificationService import easyMessage
import timeService
from time import sleep
from machine import Pin
import gc

switchPin = Pin(4, Pin.IN)
led = Pin(2, Pin.OUT)

led.on()

connect()

easyMessage('Booting up')

while(True):
    secondsUntilNextAlarm = timeService.secondsUntilNextAlarm()
    print(f"Sleeping for {secondsUntilNextAlarm} seconds")
    sleep(secondsUntilNextAlarm)
    print('Woke up')
    gc.mem_free()
    if(switchPin.value() or True):
        connect()
        w = weatherApi.apiWeather()
        isGoodWeather = weatherApi.shouldTakeBike(w)

        if(isGoodWeather):
            easyMessage("Weather looks good")
        else:
            easyMessage("Bad weather")
    else:
        easyMessage('Switch is off')  # Todo change
