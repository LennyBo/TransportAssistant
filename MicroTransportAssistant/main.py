from wifiService import connect
import weatherApi
from notificationService import easyMessage
import timeService
from machine import deepsleep
import machine
import gc
import os


switch = machine.Pin(15, machine.Pin.IN)

print(switch)

exit()

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
    if(abs(deltaSeconds) < 300):
        print("Predicting")
        print('Fetching weather')
        gc.collect()
        w = weatherApi.apiWeather()
        gc.collect()
        print('Evaluate Weather')
        
        isGoodWeather = weatherApi.shouldTakeBike(w)
        
        weather = [x for x in w.values()]
        wStr = f"In the morning: {weather[0][2]}°C - {weather[0][1]}%0A" + \
               f"In the afternoon: {weather[1][2]}°C - {weather[1][1]}"
        if(isGoodWeather):
            print('Weather looks good')
            easyMessage(f"Weather looks good%0A{wStr}")
        else:
            print('Bad weather')
            easyMessage(f"Bad weather%0A{wStr}")
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
