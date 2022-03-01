import Func_Data as daF
import ast

statepath = daF.get_str_path('statepath')
drap = daF.get_str_path('drap')
wrap = daF.get_str_path('wrap')
userpath = daF.get_str_path('userpath')
statelist = daF.get_str_path('statelist')

def reset_all():
    state_list = daF.read_lists(statelist)
    state_data = open(statepath, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    for i in range(len(state_list)):
        state_dict[state_list[i]] = 0
    f = open(statepath, 'w')
    f.write(str(state_dict))
    f.close()


def reset_states():
    state_list = daF.read_lists(statelist)
    state_data = open(statepath, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    for i in range(len(state_list)):
        state_dict[state_list[i]] = 0
    f = open(statepath, 'w')
    f.write(str(state_dict))
    f.close()


def delete_data():
    daF.data_clear(drap)
    daF.data_clear(wrap)


def reset_user():
    daF.set_data(userpath, 'u_name', ' ')
    daF.set_data(userpath, 'u_prename', ' ')
    daF.set_data(userpath, 'u_number', ' ')
    daF.set_data(userpath, 'u_pw', ' ')
