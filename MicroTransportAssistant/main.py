from wifiService import connect
import weatherApi
from notificationService import easyMessage
import timeService
from machine import deepsleep
import machine
import gc
import os


led = machine.Pin(2, machine.Pin.OUT)
led.value(1)
f = None

timeToSleep = 5 * 60 * 60 * 1000


def enableLogging():
    global f
    f = open('log.txt', 'a')
    os.dupterm(f)


def disableLogging():
    global f
    os.dupterm(None)
    f.close()

connect()

timeService.loadTime()
#print(time.mktime((2023, 9, 10, 23, 27, 36, 6, 253)))
#exit()

if(timeService.isAlarmDay()):
    deltaSeconds = timeService.deltaToAlarm()
    print(deltaSeconds)
    if(abs(deltaSeconds) < 60):
        print("Predicting")
        print('Fetching weather')
        gc.collect()
        w = weatherApi.apiWeather()
        gc.collect()
        print('Evaluate Weather')
        isGoodWeather = weatherApi.shouldTakeBike(w)

        if(isGoodWeather):
            print('Weather looks good')
            easyMessage("Weather looks good")
        else:
            print('Bad weather')
            easyMessage("Bad weather")
        print(f"Sleeping for {timeToSleep} ms")
        deepsleep(timeToSleep)
    elif(deltaSeconds < 0):
        print(f"Passed alarm time\nGoing to sleep for {timeToSleep} ms")
        deepsleep(timeToSleep)  # 5 Hours in ms
    else:
        print(f"Alarm pretty soon\nGoing to sleep for {deltaSeconds * 1000} ms")
        deepsleep(deltaSeconds * 1000)  # 5 Hours in ms
else:
    print(f"No alarm today\nGoing to sleep for {timeToSleep} ms")
    deepsleep(timeToSleep)  # 5 Hours in ms
