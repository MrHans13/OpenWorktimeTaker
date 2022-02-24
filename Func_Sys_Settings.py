import Func_Data as daF
import ast


def reset_all():
    state_list = daF.read_lists('/home/peti/Projects/OpenWtTaker/temp/list_states.txt')
    state_data = open('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    for i in range(len(state_list)):
        state_dict[state_list[i]] = 0
    f = open('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'w')
    f.write(str(state_dict))
    f.close()


def reset_states():
    state_list = daF.read_lists('/home/peti/Projects/OpenWtTaker/temp/list_states.txt')
    state_data = open('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'r')
    state_dict_str = state_data.read()
    state_data.close()
    state_dict = ast.literal_eval(state_dict_str)
    for i in range(len(state_list)):
        state_dict[state_list[i]] = 0
    f = open('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'w')
    f.write(str(state_dict))
    f.close()


def delete_data():
    daF.data_clear('/home/peti/Projects/OpenWtTaker/temp/Rap_D.txt')
    daF.data_clear('/home/peti/Projects/OpenWtTaker/temp/Rap_W.txt')


def reset_user():
    daF.set_data('/home/peti/Projects/OpenWtTaker/temp/user_hpf.txt', 'u_name', ' ')
    daF.set_data('/home/peti/Projects/OpenWtTaker/temp/user_hpf.txt', 'u_prename', ' ')
    daF.set_data('/home/peti/Projects/OpenWtTaker/temp/user_hpf.txt', 'u_number', ' ')
    daF.set_data('/home/peti/Projects/OpenWtTaker/temp/user_hpf.txt', 'u_pw', ' ')