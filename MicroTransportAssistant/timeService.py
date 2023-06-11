import ntptime
import time

GMT_OFFSET = 2 * 60 * 60

alarmsOnWeekday = [True, True, True, True, True,
                   True, True]  # Make sure it is sorted

alarmHour = 6
alarmMinute = 20


# Offset to GMT+0
alarmHour -= 2

def syncTime():
    ntptime.settime()
    

def secondsUntilNextAlarm():
    syncTime()
    t = currentTime()
    
    dayOfWeek = t[6]
    isAlarmTimePassed = not (t[3] < alarmHour or (t[3] == alarmHour and t[4] < alarmMinute))
    daysToAdd = daysUntilNextAlarm(dayOfWeek,isAlarmTimePassed)
    
    
    # Set correct time
    timeAlarm = getTimeOf(t,alarmHour,alarmMinute)
    
    epochTimeAlarm = time.mktime(timeAlarm) + daysToAdd * 24 * 60 * 60
    
    return epochTimeAlarm - time.time()
    
    
    

def daysUntilNextAlarm(weekDay,isPassedToday):
    count = 0
    if isPassedToday:
        weekDay = (weekDay + 1) % 7 # If we passed the time of alarm we start on the next day
        count += 1
    i = weekDay
    while True:
        if(not alarmsOnWeekday[i]):
            count += 1
        else:
            return count
        i = (i + 1) % 7
    
    


def currentTime():
    return time.gmtime(time.time())


def getTimeOf(t,hour,minute):
    return (t[0],t[1],t[2],hour,minute,0,t[6],t[7])