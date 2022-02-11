import dataFunc as daF


def calc_Work_Time():
    work_minutes = daF.read_Int('.min_stop.txt') - daF.read_Int('.min_start.txt')
    work_hours = daF.read_Int('.hour_stop.txt') - daF.read_Int('.hour_start.txt')
    o_t_hour_old = daF.read_Int('UeZeit.txt')
    if work_hours < 0:
        work_hours += 24
    if work_minutes < 0:
        work_minutes += 60
        work_hours -= 1
    if work_hours > 8:
        o_t_hour_new = work_hours - 8

        daF.write_Stat_Data('.ue_hour.txt',o_t_hour_new)

    daF.write_Stat_Data('.workmin.txt',str(work_minutes))
    daF.write_Stat_Data('.workhour.txt', str(work_hours))


