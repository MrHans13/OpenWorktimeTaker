import Func_Data as daF
import Func_Rap_Week as wrF


def finish_commission(tf):
    commissionstate = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'comm_state')
    workmin_ges = daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/.time_file.txt', 'workminges')
    workhour_ges = daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/.time_file.txt', 'workhourges')
    comm = daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/act_comm.txt', 'c_nr')
    day = daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/.act_date.txt', 'day')
    month = daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/.act_date.txt', 'month')
    year = daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/.act_date.txt', 'year')
    if commissionstate == 1:
        wrF.write_titel_wrap()
        wrF.a_data_wrap(day + '.' + month + '.' + year + '\tKommission: ' +
                        comm + '\t' + workhour_ges + 'h' + workmin_ges +
                        'min\n')
    if commissionstate > 1:
        wrF.a_data_wrap(day + '.' + month + '.' + year + '\tKommission: ' +
                        comm + '\t' + workhour_ges + 'h' + workmin_ges +
                        'min\n')
    wrF.weekly_rap(tf)
