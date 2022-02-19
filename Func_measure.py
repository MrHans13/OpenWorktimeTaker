import time
import Func_Data as daF
import Func_Calc as caF
import Func_Rap_Day as drF

def set_Start_Time(tf):
    filestate = daF.get_int_Data('.prog_states.txt', 'file_state')
    now = time.localtime()
    minute = str(now.tm_min)
    hour = str(now.tm_hour)
    if int(minute) < 10:
        minute = '0' + minute
    if int(hour) < 10:
        hour = '0' + hour
    daF.set_Data('.time_file.txt', 'startmin', minute)
    daF.set_Data('.time_file.txt', 'starthour', hour)
    if filestate < 3:
        drF.a_data_dRap('\t\t' + hour + ':' + minute)
        drF.dailyRap(tf)
    else:
        drF.a_data_dRap('\n\t\t\t\t' + hour + ':' + minute)
        drF.dailyRap(tf)

def set_Stop_Time(tf):
    now = time.localtime()
    minute = str(now.tm_min)
    hour = str(now.tm_hour)
    if int(minute) < 10:
        minute = '0' + minute
    if int(hour) < 10:
        hour = '0' + hour
    daF.set_Data('.time_file.txt', 'stopmin', minute)
    daF.set_Data('.time_file.txt', 'stophour', hour)
    caF.calc_Work_Time()
    w_hour = daF.get_str_Data('.time_file.txt', 'workhour')
    w_min = daF.get_str_Data('.time_file.txt', 'workmin')
    ue_Zeit = daF.get_str_Data('ue_zeit.txt', 'ue_zeit')
    drF.a_data_dRap('\t' + hour + ':' + minute + '\t' + w_hour + 'h' + w_min + 'min\t' + ue_Zeit)
    drF.dailyRap(tf)
