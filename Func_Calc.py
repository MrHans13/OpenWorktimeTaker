import Func_Data as daF


def calc_Work_Time():
    work_minutes = daF.get_int_Data('.time_file.txt', 'stopmin') - daF.get_int_Data('.time_file.txt', 'startmin')
    work_hours = daF.get_int_Data('.time_file.txt', 'stophour') - daF.get_int_Data('.time_file.txt', 'starthour')
    work_minutes_ges = daF.get_int_Data('.time_file.txt', 'workminges')
    daF.set_Data('.time_file.txt', 'workminges', str(work_minutes_ges + work_minutes))
    work_hours_ges = daF.get_int_Data('.time_file.txt', 'workhourges')
    daF.set_Data('.time_file.txt', 'workhourges', str(work_hours_ges + work_hours))

    if work_hours < 0:
        work_hours += 24
    if work_minutes < 0:
        work_minutes += 60
        work_hours -= 1
    daF.set_Data('.time_file.txt', 'workmin', work_minutes)
    daF.set_Data('.time_file.txt', 'workhour', work_hours)
    calc_O_Time()


def calc_O_Time():
    daystate = daF.get_int_Data('.prog_states.txt', 'day_state')
    workhour = daF.get_int_Data('.time_file.txt', 'workhour')
    workmin = daF.get_int_Data('.time_file.txt', 'workmin')
    ue_min = daF.get_int_Data('ue_zeit.txt', 'ue_min')
    ue_hour = daF.get_int_Data('ue_zeit.txt', 'ue_hour')
    sollzeit = daF.get_int_Data('ue_zeit.txt', 'soll_t')
    if ue_min > 60:
        ue_min -= 60
        ue_hour += 1
    if daystate == 0:
        if workhour < sollzeit:
            minuszeit = workhour - sollzeit
            ue_hour_ges = ue_hour + minuszeit
            ue_min_ges = ue_min + workmin
            daF.set_Data('ue_zeit.txt', 'ue_min', ue_min_ges)
            daF.set_Data('ue_zeit.txt', 'ue_hour', ue_hour_ges)
            daF.set_Data('ue_zeit.txt', 'ue_zeit', str(ue_hour_ges) + 'h' + str(ue_min_ges) + 'min')
            print('< 8')
    else:
        if workhour == sollzeit:
            ue_min_ges = ue_min + workmin
            daF.set_Data('ue_zeit.txt', 'ue_min', ue_min_ges)
            daF.set_Data('ue_zeit.txt', 'ue_zeit', str(ue_hour) + 'h' + str(ue_min_ges) + 'min')
            print('8')
        if workhour > sollzeit:
            pluszeit = workhour - sollzeit
            ue_hour_ges = ue_hour + pluszeit
            ue_min_ges = ue_min + workmin
            daF.set_Data('ue_zeit.txt', 'ue_zeit', str(ue_hour_ges) + 'h' + str(ue_min_ges) + 'min')
            print('>8')
