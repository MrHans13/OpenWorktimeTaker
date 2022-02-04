import dataTransfer as dat


def worktime_calc():
    wt_minute_start = dat.dataRead('.min_start.txt')
    wtminute_stop = dat.dataRead('.min_stop.txt')
    wt_hour_start = dat.dataRead('.hour_start.txt')
    wt_hour_stop = dat.dataRead('.hour_stop.txt')
    work_minutes = int(wtminute_stop) - int(wt_minute_start)
    work_hours = int(wt_hour_stop) - int(wt_hour_start)
    if work_hours < 0:
        work_hours += 24
    if work_minutes < 0:
        work_minutes += 60
        work_hours -= 1
    return str(work_hours) + 'h' + str(work_minutes) + 'min'
