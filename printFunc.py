import dataFunc as daF


def print_To_dRap():
    fileState = daF.read_Int('.fileState.txt')
    day = daF.read_Str('.day.txt')
    month = daF.read_Str('.month.txt')
    year = daF.read_Str('.year.txt')
    commision = daF.read_Str('.comm.txt')
    start_min = daF.read_Str('.min_start.txt')
    stop_min = daF.read_Str('.min_stop.txt')
    start_hour = daF.read_Str('.hour_start.txt')
    stop_hour = daF.read_Str('.hour_stop.txt')
    work_min = daF.read_Str('.workmin.txt')
    work_hour = daF.read_Str('.workhour.txt')
    o_time = daF.read_Str('UeZeit.txt')
    if fileState == 2:
        daF.write_titelDrap()
        f = open('DailyRapport.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision)
        f.close()
    if fileState == 3:
        daF.write_titelDrap()
        f = open('DailyRapport.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision + '\t\t' +
                start_hour + ':' + start_min)
        f.close()
    if fileState == 4:
        daF.write_titelDrap()
        f = open('DailyRapport.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision + '\t\t' +
                start_hour + ':' + start_min + '\t' + stop_hour +
                ':' + stop_min + '\t' + work_hour + 'h' + work_min + 'min' +
                '\t' + o_time + 'h\n')
        f.close()
    if fileState == 5:
        f = open('DailyRapport.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision + '\t\t' +
                start_hour + ':' + start_min)
        f.close()
    if fileState == 6:
        f = open('DailyRapport.txt', 'a')
        f.write('\t' + stop_hour + ':' + stop_min + '\t' + work_hour +
                'h' + work_min + 'min' + '\t' + o_time + 'h\n')
        f.close()


def factory_Reset():
    datalist = '.hour_start.txt', '.hour_stop.txt', '.min_start.txt', '.min_stop.txt', \
               '.workmin.txt', '.workhour.txt', '.comm.txt', '.day.txt', \
               '.month.txt', '.year.txt', 'DailyRapport.txt'
    statelist = '.progState.txt', '.fileState.txt', '.weekState.txt', '.dayState.txt', \
                '.workState.txt'
    for i in range(len(datalist)):
        daF.data_clear(datalist[i])
    for i in range(len(statelist)):
        daF.state_Reset(statelist[i])
