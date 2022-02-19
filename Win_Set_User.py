import tkinter as tk
import tkinter.messagebox as mBox
import Func_Data as daF


def create_User_Set_Win(win):
    # zweites Fenster config
    user_set_win = tk.Toplevel(win)
    user_set_win.geometry('400x150')
    user_set_win.resizable(width=False, height=False)

    # Labels erstellen
    label_list = ['Name    ', 'Vorname ', 'Mitarbeiter Nr.']
    for i in range(len(label_list)):
        tk.Label(user_set_win, text=label_list[i]).grid(row=i+1, column=0)
    tk.Label(user_set_win, text='Bitte füllen Sie alle Felder aus und bestätigen anschliessend.').grid(row=0, column=0, columnspan=3, pady=10)
    # Entry erstellen
    var_number, var_u_prename, var_u_name = tk.StringVar(), tk.StringVar(), tk.StringVar()
    name = tk.Entry(user_set_win, textvariable=var_u_name)
    name.grid(row=1, column=1)
    prename = tk.Entry(user_set_win, textvariable=var_u_prename)
    prename.grid(row=2, column=1)
    user_name = tk.Entry(user_set_win, textvariable=var_number)
    user_name.grid(row=3, column=1)

    # Daten in Files schreiben
    var_number.trace("w", lambda *args: daF.set_Data('user_hpf.txt', 'u_number', var_number.get()))
    var_u_name.trace("w", lambda *args: daF.set_Data('user_hpf.txt', 'u_name', var_u_name.get()))
    var_u_prename.trace("w", lambda *args: daF.set_Data('user_hpf.txt', 'u_prename', var_u_prename.get()))

    # Registrierbutton
    tk.Button(user_set_win, text='Registrieren',
              command=lambda: register_User(user_set_win, win)).grid(row=4, column=1, columnspan=2)


def register_User(win1, win2):
    mBox.showinfo('Achtung', 'Programm muss neu gestartet werden.\n'
                             'Programm beenden?')
    daF.set_Data('.prog_states.txt', 'user_state', 1)
    win1.destroy()
    win2.destroy()
