import Func_Data as daF
import Func_Rap_Week as wrF

def finish_Comm(tf):
    commstate = daF.get_int_Data('temp/.prog_states.txt', 'comm_state')
    workmin_ges = daF.get_str_Data('temp/.time_file.txt', 'workminges')
    workhour_ges = daF.get_str_Data('temp/.time_file.txt', 'workhourges')
    comm = daF.get_str_Data('temp/act_comm.txt', 'c_nr')
    day = daF.get_str_Data('temp/.act_date.txt', 'day')
    month = daF.get_str_Data('temp/.act_date.txt', 'month')
    year = daF.get_str_Data('temp/.act_date.txt', 'year')
    if commstate == 1:
        wrF.write_titelWrap()
        wrF.a_data_wRap(day + '.' + month + '.' + year + '\tKommission: ' +
                    comm + '\t' + workhour_ges + 'h' + workmin_ges +
                    'min\n')
    if commstate > 1:
        wrF.a_data_wRap(day + '.' + month + '.' + year + '\tKommission: ' +
                        comm + '\t' + workhour_ges + 'h' + workmin_ges +
                        'min\n')
    wrF.weeklyRap(tf)