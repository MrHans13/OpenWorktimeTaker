import Func_Data as daF


def add_worktime(state, newtime):
    oldtime = daF.get_int_data('temp/.time_file.txt', state)
    result = oldtime + newtime
    daF.set_data('temp/.time_file.txt', state, result)


def calc_work_hour():
    starthour = daF.get_int_data('temp/.time_file.txt', 'starthour')
    stophour = daF.get_int_data('temp/.time_file.txt', 'stophour')
    workhour = stophour - starthour
    if workhour < 0:
        workhour += 24
    daF.set_data('temp/.time_file.txt', 'workhour', workhour)


def calc_work_min():
    startmin = daF.get_int_data('temp/.time_file.txt', 'starthour')
    stopmin = daF.get_int_data('temp/.time_file.txt', 'stophour')
    workmin = stopmin - startmin
    if workmin < 0:
        workmin += 60
        workhour -= 1
    daF.set_data('temp/.time_file.txt', 'workhour', workhour)
    daF.set_data('temp/.time_file.txt', 'workmin', workmin)


def calc_work_time():
    calc_work_hour()
    calc_work_min()


def calc_over_time():
    workhour = daF.get_int_data('temp/.time_file.txt', 'workhour')
    workmin = daF.get_int_data('temp/.time_file.txt', 'workmin')
    ue_min = daF.get_int_data('temp/ue_zeit.txt', 'ue_min')
    ue_hour = daF.get_int_data('temp/ue_zeit.txt', 'ue_hour')
    sollzeit = daF.get_int_data('temp/ue_zeit.txt', 'soll_t')
    if ue_min > 60:
        ue_min -= 60
        ue_hour += 1
    if workhour < sollzeit:
        minuszeit = workhour - sollzeit
        ue_hour_ges = ue_hour + minuszeit
        ue_min_ges = ue_min + workmin
        daF.set_data('temp/ue_zeit.txt', 'ue_min', ue_min_ges)
        daF.set_data('temp/ue_zeit.txt', 'ue_hour', ue_hour_ges)
        daF.set_data('temp/ue_zeit.txt', 'ue_zeit', str(ue_hour_ges) + 'h' + str(ue_min_ges) + 'min')
        print('< 8')
    else:
        if workhour == sollzeit:
            ue_min_ges = ue_min + workmin
            daF.set_data('temp/ue_zeit.txt', 'ue_min', ue_min_ges)
            daF.set_data('temp/ue_zeit.txt', 'ue_zeit', str(ue_hour) + 'h' + str(ue_min_ges) + 'min')
            print('8')
        if workhour > sollzeit:
            pluszeit = workhour - sollzeit
            ue_hour_ges = ue_hour + pluszeit
            ue_min_ges = ue_min + workmin
            daF.set_data('temp/ue_zeit.txt', 'ue_zeit', str(ue_hour_ges) + 'h' + str(ue_min_ges) + 'min')
            print('>8')
