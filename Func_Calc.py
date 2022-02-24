import Func_Data as daF
import time


def set_time(file, state):
    now = time.localtime()
    minute = int(now.tm_min)
    hour = int(now.tm_hour)
    if state % 2 == 0:
        daF.set_data(file, 'starthour', hour)
        daF.set_data(file, 'startmin', minute)
    else:
        daF.set_data(file, 'stophour', hour)
        daF.set_data(file, 'stopmin', minute)


def add_worktime(file, state, newtime):
    oldtime = daF.get_int_data(file, state)
    result = oldtime + newtime
    daF.set_data(file, state, result)


def calc_work_hour(file):
    starthour = daF.get_int_data(file, 'starthour')
    stophour = daF.get_int_data(file, 'stophour')
    workhour = stophour - starthour
    if workhour < 0:
        workhour += 24
    daF.set_data(file, 'workhour', workhour)
    return workhour

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
    return workmin

def calc_work_time(file):
    calc_work_hour(file)
    calc_work_min(file)


def calc_over_time():
    workhour = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.time_file.txt', 'workhour')
    workmin = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.time_file.txt', 'workmin')
    ue_min = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_min')
    ue_hour = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_hour')
    sollzeit = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'soll_t')
    if ue_min > 60:
        ue_min -= 60
        ue_hour += 1
    if workhour < sollzeit:
        minuszeit = workhour - sollzeit
        ue_hour_ges = ue_hour + minuszeit
        ue_min_ges = ue_min + workmin
        daF.set_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_min', ue_min_ges)
        daF.set_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_hour', ue_hour_ges)
        daF.set_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_zeit', str(ue_hour_ges) + 'h' + str(ue_min_ges) + 'min')
        print('< 8')
    else:
        if workhour == sollzeit:
            ue_min_ges = ue_min + workmin
            daF.set_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_min', ue_min_ges)
            daF.set_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_zeit', str(ue_hour) + 'h' + str(ue_min_ges) + 'min')
            print('8')
        if workhour > sollzeit:
            pluszeit = workhour - sollzeit
            ue_hour_ges = ue_hour + pluszeit
            ue_min_ges = ue_min + workmin
            daF.set_data('/home/peti/Projects/OpenWtTaker/temp/ue_zeit.txt', 'ue_zeit', str(ue_hour_ges) + 'h' + str(ue_min_ges) + 'min')
            print('>8')
