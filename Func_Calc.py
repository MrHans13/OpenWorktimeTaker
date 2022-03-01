import time
import Func_Data as daF
import Func_Rap_Day as drF


def set_time(file, state):
    commstate = daF.get_int_data(daF.get_str_path('statepath'), 'comm_state')
    now = time.localtime()
    minute = int(now.tm_min)
    hour = int(now.tm_hour)
    if state % 2 == 0:
        daF.set_data(file, 'starthour', hour)
        daF.set_data(file, 'startmin', minute)
        if minute < 10:
            minute = '0' + str(minute)
        if hour < 10:
            hour = '0' + str(hour)
        if commstate == 0:
            drF.a_data_drap(str(hour) + '.' + str(minute))
        else:
            drF.a_data_drap('\t\t\t' + str(hour) + '.' + str(minute))
    else:
        daF.set_data(file, 'stophour', hour)
        daF.set_data(file, 'stopmin', minute)
        if minute < 10:
            minute = '0' + str(minute)
        if hour < 10:
            hour = '0' + str(hour)
        if commstate == 0:
            drF.a_data_drap('\t' + str(hour) + '.' + str(minute))
        else:
            drF.a_data_drap('\t' + str(hour) + '.' + str(minute) + '\n')

def add_worktime(file, state, newtime):
    oldtime = daF.get_int_data(file, state)
    result = int(oldtime) + newtime
    daF.set_data(file, state, result)


def calc_work_hour(file):
    starthour = daF.get_int_data(file, 'starthour')
    stophour = daF.get_int_data(file, 'stophour')
    workhour = stophour - starthour
    if workhour < 0:
        workhour += 24
    daF.set_data(file, 'workhour', workhour)


def calc_work_min(file):
    workhour = daF.get_int_data(file, 'workhour')
    startmin = daF.get_int_data(file, 'startmin')
    stopmin = daF.get_int_data(file, 'stopmin')
    workmin = stopmin - startmin
    if workmin < 0:
        workmin += 60
        workhour -= 1
    daF.set_data(file, 'workhour', workhour)
    daF.set_data(file, 'workmin', workmin)


def calc_work_time(file):
    calc_work_hour(file)
    calc_work_min(file)
