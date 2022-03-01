import ast
import time
import datetime

actdate = '/home/huuspi/Projects/OpenWorktimeTaker/temp/.act_date.txt'


def get_act_date():
    state_data = open(actdate, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    day = state_dict['day']
    month = state_dict['month']
    year = state_dict['year']
    date = day + '.' + month + '.' + year
    return date


def set_act_date():
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
    f = open(actdate, 'w')
    f.write(str(date_dict))
    f.close()
    return day + '.' + month + '.' + year


def set_data(file, keyword, s):
    state_data = open(file, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    state_dict[keyword] = s
    f = open(file, 'w')
    f.write(str(state_dict))
    f.close()


def get_str_data(file, state):
    state_data = open(file, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    act_state = state_dict[state]
    return str(act_state)


def get_str_path(state):
    state_data = open('/home/huuspi/Projects/OpenWorktimeTaker/temp/paths.txt', 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    act_state = state_dict[state]
    return str(act_state)


def get_int_data(file, keyword):
    state_data = open(file, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    act_state = state_dict[keyword]
    return int(act_state)


def read_lists(list_file):
    comm_list_file = open(list_file, 'r')
    comm_list = comm_list_file.read().split()
    comm_list_file.close()
    return comm_list


def data_clear(textfile):
    f = open(textfile, 'w')
    f.write('')
    f.close()


def data_temp_clear(textfile):
    f = open('/home/huuspi/Projects/OpenWorktimeTaker/temp/' + textfile, 'w')
    f.write(' ')
    f.close()
