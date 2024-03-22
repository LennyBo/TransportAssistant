import ntptime
import time

alarmsOnWeekday = [False, True, True, True, True, False, False]  # Make sure it is sorted

alarmHour = 6
alarmMinute = 25


# Offset to GMT+0
alarmHour -= 2


max_retries = 3
retry_delay = 5  # seconds

tEpoch = 0

def loadTime():
    global tEpoch
    tEpoch = ntptime.time()

def deltaToAlarm():
    t = currentTime()
    print("t",t)
    timeAlarm = getTimeOf(t,alarmHour,alarmMinute)
    print("timeAlarm", timeAlarm)
    epochTimeAlarm = time.mktime(timeAlarm)
    print("epochTimeAlarm", epochTimeAlarm)
    return epochTimeAlarm - tEpoch
    

def isAlarmDay():
    t = currentTime()
    dayOfWeek = t[6]
    return alarmsOnWeekday[dayOfWeek]

def currentTime():
    return time.gmtime(tEpoch)


def getTimeOf(t,hour,minute):
    return (t[0],t[1],t[2],hour,minute,0,t[6],t[7])