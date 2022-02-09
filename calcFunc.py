import dataFunc as daF


def calc_Work_Time():
    work_minutes = daF.read_Int('.min_stop.txt') - daF.read_Int('.min_start.txt')
    work_hours = daF.read_Int('.hour_stop.txt') - daF.read_Int('.hour_start.txt')
    if work_hours < 0:
        work_hours += 24
    if work_minutes < 0:
        work_minutes += 60
        work_hours -= 1
    daF.write_Stat_Data('.workmin.txt',str(work_minutes))
    daF.write_Stat_Data('.workhour.txt', str(work_hours))


