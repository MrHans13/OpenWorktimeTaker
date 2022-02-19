import ast
import time
import datetime


def get_Act_Date():
    state_data = open('.act_date.txt', 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    day = state_dict['day']
    month = state_dict['month']
    year = state_dict['year']
    date = day + '.' + month + '.' + year
    return date


def set_Act_Date():
    now = time.localtime()
    day = str(now.tm_mday)
    month = str(now.tm_mon)
    year = str(now.tm_year)
    kw = datetime.date.today().isocalendar()[1]
    if int(day) < 10:
        day = '0' + day
    if int(month) < 10:
        month = '0' + month
    date_dict = {'day': day, 'month': month, 'year': year, 'kw': str(kw)}
    f = open('.act_date.txt', 'w')
    f.write(str(date_dict))
    f.close()
    return day + '.' + month + '.' + year


def set_Data(file, state, s):
    state_data = open(file, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    state_dict[state] = s
    f = open(file, 'w')
    f.write(str(state_dict))
    f.close()


def get_str_Data(file, state):
    state_data = open(file, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    act_state = state_dict[state]
    return str(act_state)


def get_int_Data(file, state):
    state_data = open(file, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    act_state = state_dict[state]
    return int(act_state)


def read_List(list_file):
    comm_list_file = open(list_file, 'r')
    comm_list = comm_list_file.read().split()
    comm_list_file.close()
    return comm_list


def data_clear(textfile):
    f = open(textfile, 'w')
    f.write('')
    f.close()


def data_temp_clear(textfile):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'w')
    f.write(' ')
    f.close()



