import Func_Data as daF
import ast


def read_Dict(file):
    state_data = open(file, 'r')
    state_dict_str = state_data.read()
    state_data.close()
    return state_dict_str


def reset_All():
    state_list = daF.read_List('list_states.txt')
    state_data = open('.prog_states.txt', 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    for i in range(len(state_list)):
        state_dict[state_list[i]] = 0
    f = open('.prog_states.txt', 'w')
    f.write(str(state_dict))
    f.close()


def reset_Stats():
    state_list = daF.read_List('list_states.txt')
    state_data = open('.prog_states.txt', 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    for i in range(len(state_list)):
        state_dict[state_list[i]] = 0
    f = open('.prog_states.txt', 'w')
    f.write(str(state_dict))
    f.close()

def delete_Data():
    daF.data_clear('Rap_D.txt')
    daF.data_clear('Rap_W.txt')


def reset_User():
    daF.set_Data('user_hpf.txt', 'u_name', ' ')
    daF.set_Data('user_hpf.txt', 'u_prename', ' ')
    daF.set_Data('user_hpf.txt', 'u_number', ' ')
    daF.set_Data('user_hpf.txt', 'u_pw', ' ')
