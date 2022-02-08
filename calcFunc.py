import dataFunc as daF


def calc_Work_Time():
    wt_minute_start = daF.read_Int('.min_start.txt')
    wtminute_stop = daF.read_Int('.min_stop.txt')
    wt_hour_start = daF.read_Int('.hour_start.txt')
    wt_hour_stop = daF.read_Int('.hour_stop.txt')
    work_minutes = wtminute_stop - wt_minute_start
    work_hours = wt_hour_stop - wt_hour_start
    if work_hours < 0:
        work_hours += 24
    if work_minutes < 0:
        work_minutes += 60
        work_hours -= 1
    daF.write_Stat_Data('.workmin.txt',str(work_minutes))
    daF.write_Stat_Data('.workhour.txt', str(work_hours))
