import time
import dataTransfer as dat

statecounter = 0
filestate = 0


def set_Date():
    now = time.localtime()
    day = str(now.tm_mday)
    month = str(now.tm_mon)
    year = str(now.tm_year)
    if int(day) < 10:
        day = str(0) + day
    if int(month) < 10:
        month = str(0) + month
    return day + '.' + month + '.' + year


def set_Time():
    global statecounter
    set_Hour()
    set_Min()
    statecounter += 1


def set_Min():
    global statecounter
    now = time.localtime()
    minute = str(now.tm_min)
    if statecounter % 2 == 0:
        dat.dataWrite('.min_start.txt', minute)
    if statecounter % 2 == 1:
        dat.dataWrite('.min_stop.txt', minute)
    if int(minute) < 10:
        return str(0) + minute
    else:
        return minute


def set_Hour():
    now = time.localtime()
    hour = str(now.tm_hour)
    if statecounter % 2 == 0:
        dat.dataWrite('.hour_start.txt', hour)
    if statecounter % 2 == 1:
        dat.dataWrite('.hour_stop.txt', hour)
    if int(hour) < 10:
        return str(0) + hour
    else:
        return hour
