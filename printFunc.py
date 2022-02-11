import dataFunc as daF
import day_R_Func as drF

def print_To_dRap():
    fileState = daF.read_Int('.state_file.txt')
    day = daF.read_Str('.day.txt')
    month = daF.read_Str('.month.txt')
    year = daF.read_Str('.year.txt')
    commision = daF.read_Str('.act_com.txt')
    start_min = daF.read_Str('.min_start.txt')
    stop_min = daF.read_Str('.min_stop.txt')
    start_hour = daF.read_Str('.hour_start.txt')
    stop_hour = daF.read_Str('.hour_stop.txt')
    work_min = daF.read_Str('.workmin.txt')
    work_hour = daF.read_Str('.workhour.txt')
    o_time = daF.read_Str('UeZeit.txt')
    if fileState == 2:
        drF.write_titelDrap()
        daF.append_Data('DailyRapport.txt', day + '.' + month + '.' + year + '\t\t' + commision)

    if fileState == 3:
        drF.write_titelDrap()
        f = open('DailyRapport.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision + '\t\t' +
                start_hour + ':' + start_min)
        f.close()
    if fileState == 4:
        drF.write_titelDrap()
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


