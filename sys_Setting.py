import dataFunc as daF
import day_R_Func as drF


def reset_Factory():
    com_list = daF.read_List('.com_file_list.txt')
    state_list = daF.read_List('.list_state_files.txt')
    user_list = daF.read_List('.user_file_list.txt')
    for i in range(len(com_list)):
        daF.data_clear(com_list[i])
    for i in range(len(state_list)):
        daF.state_Reset(state_list[i])
    for i in range(len(user_list) - 1):
        daF.data_clear(user_list[i])
    daF.write_Stat_Data(user_list[3], '0')


def reset_User():
    user_list = daF.read_List('.user_file_list.txt')
    for i in range(len(user_list) - 1):
        daF.data_clear(user_list[i])
    daF.state_Reset('.state_user.txt')


def reset_data(textfeldday):
    com_list = daF.read_List('.com_file_list.txt')
    for i in range(len(com_list)):
        daF.data_clear(com_list[i])
    daF.write_Stat_Data('.state_file.txt', '0')
    drF.dailyRap(textfeldday)


def reset_Stats():
    state_list = daF.read_List('.list_state_files.txt')
    for i in range(len(state_list)):
        daF.state_Reset(state_list[i])
