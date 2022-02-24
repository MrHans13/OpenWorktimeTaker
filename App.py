import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as mbox
import time
import Func_Button as buF
import Func_Calc as caF
import Func_Data as daF
import Func_Labels as laF
import Func_Menu as meF
import Func_Raster as raF
import Func_Rap_Week as wrF
import Func_Rap_Day as drF
import Func_Sys_Settings as syS
import Win_Set_User as seU


def tick():
    global acttime
    newtime = time.strftime('%H:%M:%S')
    if newtime != acttime:
        acttime = newtime
        labelUhr.config(text=acttime)
    labelUhr.after(200, tick)


def pushtimebutton():
    comm_state = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'comm_state')
    work_state = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'work_state')
    file_state = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'file_state')
    act_comm = daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/act_comm.txt', 'c_nr')
    if comm_state == 0:
        mbox.showinfo('Achtung', 'bitte erst\nKommission auswählen...')
    else:
        if work_state == 0:
            daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'work_state', 1)
            caF.set_time('/home/peti/Projects/OpenWtTaker/Commisions/' + act_comm + '.txt', work_state)
            timebutton_text.set('Stop')
            style_On_Off.configure("onOff.TButton", background='red')
            if file_state >= 1:
                daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'file_state', file_state + 1)
        else:
            daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'work_state', 0)
            timebutton_text.set('Start')
            style_On_Off.configure("onOff.TButton", background='green')
            reply = mbox.askyesno('Achtung', 'Wollen Sie die kommission beenden?')
            caF.set_time('/home/peti/Projects/OpenWtTaker/Commisions/' + act_comm + '.txt', work_state)
            caF.calc_work_time('/home/peti/Projects/OpenWtTaker/Commisions/' + act_comm + '.txt')
            if reply:
                daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'comm_state', 0)
            else:
                if file_state >= 2:
                    daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'file_state', file_state + 1)
                    caF.add_worktime('/home/peti/Projects/OpenWtTaker/Commisions/' + act_comm + '.txt', 'c_workmin', caF.calc_work_min('/home/peti/Projects/OpenWtTaker/Commisions/' + act_comm + '.txt'))
                    caF.add_worktime('/home/peti/Projects/OpenWtTaker/Commisions/' + act_comm + '.txt', 'c_workhour', caF.calc_work_hour('/home/peti/Projects/OpenWtTaker/Commisions/' + act_comm + '.txt'))


def change_background():
    global bgstate
    if bgstate % 2 == 0:
        main_window.config(bg=l_grey)
        style_notebook.configure("BW.TLabel", background=l_grey, foreground=d_grey)
        style_titel.configure("tS.TLabel", background=l_grey, foreground=d_grey)
        style_L_small.configure("SL.TLabel", background=l_grey, foreground=d_grey)
        style_B_small.configure("bstyle.TButton", background=l_grey, foreground=d_grey)
        style_raster_hor.configure("rSh.TLabel", background=l_grey, width=2)
        style_raster_ver.configure("rSv.TLabel", background=l_grey, width=2)
        meF.menutaskbar(main_window, l_grey, d_grey, open_file)
        bg_col_stat.set('Dark')
        bgstate += 1
    else:
        main_window.config(bg=d_grey)
        style_notebook.configure("BW.TLabel", background=d_grey, foreground=d_grey)
        style_titel.configure("tS.TLabel", background=d_grey, foreground=l_grey)
        style_L_small.configure("SL.TLabel", background=d_grey, foreground=l_grey)
        style_B_small.configure("bstyle.TButton", background=d_grey, foreground=l_grey)
        style_raster_hor.configure("rSh.TLabel", background=d_grey)
        style_raster_ver.configure("rSv.TLabel", background=d_grey, width=2)
        meF.menutaskbar(main_window, d_grey, l_grey, open_file)
        bg_col_stat.set('Light')
        bgstate += 1


def select_com(msg, selectedcomm):
    reply = mbox.askyesno('Bestätigen', msg)
    if reply:
        daF.set_data('/home/peti/Projects/OpenWtTaker/temp/act_comm.txt', 'c_nr', selectedcomm)
        workstate = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'work_state')
        filestate = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'file_state')
        if workstate == 1:
            mbox.showinfo('Achtung', 'Sie müssen erst Zeit stoppen.')
        else:
            daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'comm_state', 1)
            if filestate == 1:
                drF.a_data_drap(str(daF.set_act_date()))
                drF.a_data_drap('\t\t' + selectedcomm)
                drF.write_daily_tf(textfeldday)
            if filestate > 1:
                daF.set_data('/home/peti/Projects/OpenWtTaker/temp/act_comm.txt', 'c_nr', selectedcomm)
                daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'file_state', 2)
                drF.a_data_drap('\n' + str(daF.set_act_date()))
                drF.a_data_drap('\t\t' + selectedcomm)
                drF.write_daily_tf(textfeldday)


def items_selected(event):
    selected_indices = listbox.curselection()  # get selected indices
    selected_comms = ",".join([listbox.get(index1) for index1 in selected_indices])  # get selected items
    msg = f'Wollen Sie: {selected_comms} auswählen?'
    select_com(msg, selected_comms)


def open_file():
    tf = filedialog.askopenfilename(
        initialdir="/home/peti/Projects/OpenWtTaker/Commisions/",
        title="Open Text file",
        filetypes=(("Text Files", "*.*"),),
    )
    tf = open(tf, 'r')
    data = tf.read()
    textfeldweek.insert(END, data)
    tf.close()


def check_timebutton_state():
    work_state = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'work_state')
    if work_state == 0:
        timebutton_text.set('Start')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 12), background='green', foreground='black')
    else:
        timebutton_text.set('Stop')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 12), background='red', foreground='black')


def check_user_state():
    user_state = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'user_state')
    if user_state == 0:
        mbox.showinfo('Achtung', 'Kein User registriert.\n'
                                 'User registrieren')
        seU.create_user_set_win(main_window)
    daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'prog_state', 1)


def check_prog_state():
    progstate = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'prog_state')
    filestate = daF.get_int_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'file_state')
    if progstate == 1:
        if filestate == 0:
            drF.write_titel_drap()
            daF.set_data('/home/peti/Projects/OpenWtTaker/temp/.prog_states.txt', 'file_state', 1)
            drF.write_daily_tf(textfeldday)
        else:
            drF.write_daily_tf(textfeldday)


################################################################################
# Main Window start
################################################################################
if __name__ == "__main__":

    main_window = tk.Tk()
    main_window.title("Open Worktime Tracker")
    main_window.geometry('790x510')
    main_window.minsize(width=790, height=565)
    bgstate = 0
    d_grey = '#2b2b2b'
    l_grey = '#5c5c5c'

    main_window.configure(bg=d_grey)

    # variables
    timebutton_text = tk.StringVar()
    u_name = tk.StringVar(value=daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/user_hpf.txt', 'u_name'))
    u_prename = tk.StringVar(value=daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/user_hpf.txt', 'u_prename'))
    u_number = tk.StringVar(value=daF.get_str_data('/home/peti/Projects/OpenWtTaker/temp/user_hpf.txt', 'u_number'))
    comm_list = daF.read_lists('/home/peti/Projects/OpenWtTaker/temp/.list_commisions.txt')
    comm_list_var = tk.StringVar(value=comm_list)
    bg_col_stat = tk.StringVar(value='Light')
    act_date = tk.StringVar(value=daF.get_act_date())
    # Pictures
    logo = tk.PhotoImage(file='/home/peti/Projects/OpenWtTaker/picture/logo_001.1.png')
    notepic = tk.PhotoImage(file='/home/peti/Projects/OpenWtTaker/picture/note_bg.png')

    # Styles
    style_L_small = ttk.Style()
    style_L_small.configure("SL.TLabel", font=('Calibri', 14), background=d_grey, foreground=l_grey)
    style_titel = ttk.Style()
    style_titel.configure("tS.TLabel", font=('Calibri', 20), background=d_grey, foreground=l_grey)
    style_B_small = ttk.Style()
    style_B_small.configure("bstyle.TButton", font=('Calibri', 12), background=d_grey, foreground=l_grey)
    style_notebook = ttk.Style()
    style_notebook.configure("BW.TLabel", background=d_grey, foreground=l_grey)
    style_On_Off = ttk.Style()
    style_On_Off.configure("onOff.TButton", font=('Calibri', 12), background='green', foreground=d_grey)
    style_raster_hor = ttk.Style()
    style_raster_hor.configure("rSh.TLabel", background=d_grey, width=2)
    style_raster_ver = ttk.Style()
    style_raster_ver.configure("rSv.TLabel", background=d_grey, width=25)

    # notebook
    notebook = ttk.Notebook(main_window, style="BW.TLabel")
    notebook.grid(row=0, column=0)
    fdRap = ttk.Frame(notebook, style="BW.TLabel")
    fwRap = ttk.Frame(notebook, style="BW.TLabel")
    fComm = ttk.Frame(notebook, style="BW.TLabel")
    fSett = ttk.Frame(notebook, style="BW.TLabel")

    # Notebook Frames erstellen mit Logo und Titel
    frameList = [fdRap, fwRap, fComm, fSett]
    note_list = ['Tagesrapport', 'Wochenrapport', 'Kommission', 'Einstellungen']
    for i in range(len(frameList)):
        notebook.add(frameList[i], text=note_list[i], image=notepic, compound='center')
        raF.raster_vert(frameList[i], "rSv.TLabel")
        raF.raster_hor(frameList[i], "rSh.TLabel")
        laF.label_logo(frameList[i], logo, "BW.TLabel")
        laF.label_titel(frameList[i], note_list[i], "tS.TLabel")

    ###########################################################
    # TagesrapportSeite
    ###########################################################
    meF.menutaskbar(main_window, d_grey, l_grey, open_file)

    # Uhr
    labelUhr = ttk.Label(fdRap, style="SL.TLabel")
    labelUhr.grid(row=2, column=3, sticky='nw')
    acttime = ''
    ttk.Label(fdRap, textvariable=act_date, style="SL.TLabel").grid(row=1, column=3, sticky='sw')

    # Mitarbeiter Label erstellen
    label_list = ["Mitarbeiter Nr.", "Name", "Vorname", "", "Kommission"]
    for index in range(len(label_list)):
        laF.label_small(fdRap, label_list[index], "SL.TLabel", index + 4, 1)
    user_list = [u_number, u_name, u_prename]
    for i in range(len(user_list)):
        laF.label_interact(fdRap, user_list[i], "SL.TLabel", i + 4, 2)

    listbox = Listbox(fdRap, listvariable=comm_list_var, height=10, selectmode='browse')
    listbox.grid(row=9, column=1, padx=5, rowspan=7, sticky='W')
    listbox.bind('<<ListboxSelect>>', items_selected)

    textfeldday = Text(fdRap, height=10, width=65)
    textfeldday.grid(row=9, column=2, rowspan=7, columnspan=4, padx=5, sticky='W')

    buF.time_button(fdRap, timebutton_text, "onOff.TButton", pushtimebutton)
    ################################################################################
    # Wochenrapportseite
    ################################################################################
    textfeldweek = Text(fwRap, width=92, height=18)
    textfeldweek.grid(row=4, column=1, padx=5)
    buF.com_button(fwRap, 'Wochenrapport', notepic, "bstyle.TButton", wrF.weekly_rap(textfeldweek), 3, 1)

    ################################################################################
    # Kommissionsseite
    ################################################################################
    comm_det_lab = ['Kom.Nr.', 'Adresse', 'Ort/Plz']
    laF.label_titel(fComm, 'Aktuelle Kommission', "tS.TLabel")
    for num in range(3):
        laF.label_small(fComm, comm_det_lab[num], "SL.TLabel", num + 3, 1)

    ################################################################################
    # Einstellungsseite
    ################################################################################
    dat_name_l = ['Programm          ',
                  'Daten löschen     ',
                  'User löschen      ',
                  'Werkszustand      ']
    dat_func_l = [syS.reset_states, syS.delete_data, syS.reset_user, syS.reset_all]
    laF.label_small(fSett, 'Styling ändern    ', "SL.TLabel", 7, 1)
    buF.com_button_interact(fSett, bg_col_stat, notepic, "bstyle.TButton", change_background, 7, 2)

    buF.com_button(fSett, 'Userdaten ändern  ', notepic, "bstyle.TButton",
                   lambda: seU.create_user_set_win(main_window), 12, 2)
    for i in range(len(dat_name_l)):
        laF.label_small(fSett, dat_name_l[i], "SL.TLabel", i + 8, 1)
        buF.com_button(fSett, dat_name_l[i], notepic, "bstyle.TButton", dat_func_l[i], i + 8, 2)

    tick()
    check_timebutton_state()
    check_user_state()
    check_prog_state()
    main_window.mainloop()
