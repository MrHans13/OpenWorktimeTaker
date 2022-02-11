import tkinter as tk

import dataFunc as daF


def create_User_Set_Win(win):
    user_set_win = tk.Toplevel(win)
    user_set_win.geometry('500x300')
    # Labels erstellen
    label_list = ['Name:    ', 'Vorname: ', 'Username:']
    for i in range(len(label_list)):
        tk.Label(user_set_win, text=label_list[i]).grid(row=i, column=0)
    # Entry erstellen
    var_name, var_prename, var_u_name = tk.StringVar(), tk.StringVar(), tk.StringVar()
    name = tk.Entry(user_set_win, textvariable=var_name)
    name.grid(row=0, column=1)
    prename = tk.Entry(user_set_win, textvariable=var_prename)
    prename.grid(row=1, column=1)
    user_name = tk.Entry(user_set_win, textvariable=var_u_name)
    user_name.grid(row=2, column=1)

    var_u_name.trace("w", lambda *args: daF.write_Stat_Data('.user_name.txt', var_name.get()))
    var_u_name.trace("w", lambda *args: daF.write_Stat_Data('.user_prename.txt', var_prename.get()))
    var_u_name.trace("w", lambda *args: daF.write_Stat_Data('.user_nr.txt', var_u_name.get()))

    # Registrierbutton
    tk.Button(user_set_win, text='Registrieren',
              command=lambda: register_User(user_set_win)).grid(row=3, column=1, columnspan=2)


def register_User(win):
    daF.write_Stat_Data('.state_user.txt', '1')
    daF.write_Stat_Data('.state_prog.txt', '1')
    win.destroy()
