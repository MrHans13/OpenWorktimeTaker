import time
import dataFunc as daF


def set_Date():
    now = time.localtime()
    day = str(now.tm_mday)
    month = str(now.tm_mon)
    year = str(now.tm_year)
    if int(day) < 10:
        day = '0' + day
    if int(month) < 10:
        month = '0' + month
    daF.write_Stat_Data('.act_day.txt', day)
    daF.write_Stat_Data('.act_month.txt', month)
    daF.write_Stat_Data('.act_year.txt', year)


def set_Start_Time():
    now = time.localtime()
    minute = str(now.tm_min)
    hour = str(now.tm_hour)
    if int(minute) < 10:
        minute = '0' + minute
    if int(hour) < 10:
        hour = '0' + hour
    daF.write_Stat_Data('.m_start.txt', minute)
    daF.write_Stat_Data('.h_start.txt', hour)


def set_Stop_Time():
    now = time.localtime()
    minute = str(now.tm_min)
    hour = str(now.tm_hour)
    if int(minute) < 10:
        minute = '0' + minute
    if int(hour) < 10:
        hour = '0' + hour
    daF.write_Stat_Data('.m_stop.txt', minute)
    daF.write_Stat_Data('.h_stop.txt', hour)
