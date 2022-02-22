import time
import Func_Data as daF


def set_start_time():
    now = time.localtime()
    minute = int(now.tm_min)
    hour = int(now.tm_hour)
    daF.set_data('temp/.time_file.txt', 'starthour', hour)
    daF.set_data('temp/.time_file.txt', 'startmin', minute)


def set_stop_time():
    now = time.localtime()
    minute = int(now.tm_min)
    hour = int(now.tm_hour)
    daF.set_data('temp/.time_file.txt', 'stophour', hour)
    daF.set_data('temp/.time_file.txt', 'stopmin', minute)


def set_time(state):
    now = time.localtime()
    minute = int(now.tm_min)
    hour = int(now.tm_hour)
    if state % 2 == 0:
        daF.set_data('temp/.time_file.txt', 'starthour', hour)
        daF.set_data('temp/.time_file.txt', 'startmin', minute)
    else:
        daF.set_data('temp/.time_file.txt', 'stophour', hour)
        daF.set_data('temp/.time_file.txt', 'stopmin', minute)
