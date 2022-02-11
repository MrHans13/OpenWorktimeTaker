import dataFunc as daF
import day_R_Func as drF

def print_To_dRap():
    fileState = daF.r_Int_temp('.state_file.txt')
    day = daF.r_Str_temp('.act_day.txt')
    month = daF.r_Str_temp('.act_month.txt')
    year = daF.r_Str_temp('.act_year.txt')
    commision = daF.r_Str_temp('.act_com.txt')
    start_min = daF.r_Str_temp('.m_start.txt')
    stop_min = daF.r_Str_temp('.m_stop.txt')
    start_hour = daF.r_Str_temp('.h_start.txt')
    stop_hour = daF.r_Str_temp('.h_stop.txt')
    work_min = daF.r_Str_temp('.m_work.txt')
    work_hour = daF.r_Str_temp('.h_work.txt')
    o_time = daF.r_Str_temp('.ue_zeit.txt')
    if fileState == 2:
        drF.write_titelDrap()
        daF.append_Data('Rap_D.txt', day + '.' + month + '.' + year + '\t\t' + commision)

    if fileState == 3:
        drF.write_titelDrap()
        f = open('Rap_D.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision + '\t\t' +
                start_hour + ':' + start_min)
        f.close()
    if fileState == 4:
        drF.write_titelDrap()
        f = open('Rap_D.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision + '\t\t' +
                start_hour + ':' + start_min + '\t' + stop_hour +
                ':' + stop_min + '\t' + work_hour + 'h' + work_min + 'min' +
                '\t' + o_time + 'h\n')
        f.close()
    if fileState == 5:
        f = open('Rap_D.txt', 'a')
        f.write(day + '.' + month + '.' + year + '\t\t' + commision + '\t\t' +
                start_hour + ':' + start_min)
        f.close()
    if fileState == 6:
        f = open('Rap_D.txt', 'a')
        f.write('\t' + stop_hour + ':' + stop_min + '\t' + work_hour +
                'h' + work_min + 'min' + '\t' + o_time + 'h\n')
        f.close()


