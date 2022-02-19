#!/usr/bin/env python

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as mbox
import time
import Func_Button as buF
import Func_Data as daF
import Func_Labels as laF
import Func_measure as mef
import Func_Menu as meF
import Func_Raster as raF
import Func_Rap_Week as wrF
import Func_Rap_Day as drF
import Func_Sys_Settings as syS
import Func_Comm as coF
import Win_Set_User as seU


def tick():
    global zeit
    neuezeit = time.strftime('%H:%M:%S')
    if neuezeit != zeit:
        zeit = neuezeit
        labelUhr.config(text=zeit)
    labelUhr.after(200, tick)


def push_Timebutton():
    work_state = daF.get_int_Data('.prog_states.txt', 'work_state')
    comm_state = daF.get_int_Data('.prog_states.txt', 'comm_state')
    file_state = daF.get_int_Data('.prog_states.txt', 'file_state')
    if comm_state == 0:
        mbox.showinfo('Achtung', 'bitte erst\nKommission auswählen...')
    else:
        if work_state == 0:
            mef.set_Start_Time(textfeldday)
            timebut_text.set('Stop')
            style_On_Off.configure("onOff.TButton", background='red')
            daF.set_Data('.prog_states.txt', 'work_state', 1)
            daF.set_Data('.prog_states.txt', 'tBut_state', 1)
            if file_state >= 1:
                daF.set_Data('.prog_states.txt', 'file_state', file_state + 1)
        else:
            reply = mbox.askyesno('Achtung', 'Wollen Sie die kommission beenden?')
            if reply:
                mef.set_Stop_Time(textfeldday)
                timebut_text.set('Start')
                style_On_Off.configure("onOff.TButton", background='green')
                daF.set_Data('.prog_states.txt', 'work_state', 0)
                daF.set_Data('.prog_states.txt', 'tBut_state', 0)
                daF.set_Data('.prog_states.txt', 'comm_state', comm_state + 1)
                coF.finish_Comm(textfeldweek)

            else:
                mef.set_Stop_Time(textfeldday)
                timebut_text.set('Start')
                style_On_Off.configure("onOff.TButton", background='green')
                daF.set_Data('.prog_states.txt', 'work_state', 0)
                daF.set_Data('.prog_states.txt', 'tBut_state', 0)
                if file_state >= 2:
                    daF.set_Data('.prog_states.txt', 'file_state', file_state + 1)


def changeBackground():
    global bgstate
    if bgstate % 2 == 0:
        main_window.config(bg=light_grey)
        style_notebook.configure("BW.TLabel", background=light_grey, foreground=dark_grey)
        style_titel.configure("tS.TLabel", background=light_grey, foreground=light_grey)
        style_L_small.configure("SL.TLabel", background=light_grey, foreground=dark_grey)
        style_B_small.configure("bstyle.TButton", background=light_grey, foreground=light_grey)
        style_raster_hor.configure("rSh.TLabel", background=light_grey, width=2)
        style_raster_ver.configure("rSv.TLabel", background=light_grey, width=2)
        meF.menutaskbar(main_window, light_grey, dark_grey, openFile)
        bg_col_stat.set('Dark')
        bgstate += 1
    else:
        main_window.config(bg=dark_grey)
        style_notebook.configure("BW.TLabel", background=dark_grey, foreground=dark_grey)
        style_titel.configure("tS.TLabel", background=dark_grey, foreground=light_grey)
        style_L_small.configure("SL.TLabel", background=dark_grey, foreground=light_grey)
        style_B_small.configure("bstyle.TButton", background=dark_grey, foreground=light_grey)
        style_raster_hor.configure("rSh.TLabel", background=dark_grey)
        style_raster_ver.configure("rSv.TLabel", background=dark_grey, width=2)
        meF.menutaskbar(main_window, dark_grey, light_grey, openFile)
        bg_col_stat.set('Light')
        bgstate += 1


def select_Com(msg, scomm):
    reply = mbox.askyesno('Bestätigen', msg)
    if reply:
        workstate = daF.get_int_Data('.prog_states.txt', 'work_state')
        filestate = daF.get_int_Data('.prog_states.txt', 'file_state')
        if workstate == 1:
            mbox.showinfo('Achtung', 'Sie müssen erst Zeit stoppen.')
        else:
            if filestate == 1:
                daF.set_Data('act_comm.txt', 'c_nr', scomm)
                drF.a_data_dRap(str(daF.set_Act_Date()))
                drF.a_data_dRap('\t\t' + scomm)
                drF.dailyRap(textfeldday)
                daF.set_Data('.prog_states.txt', 'comm_state', 1)
                daF.set_Data('.prog_states.txt', 'week_state', 1)
                daF.set_Data('.prog_states.txt', 'day_state', 1)
            if filestate > 1:
                daF.set_Data('act_comm.txt', 'c_nr', scomm)
                daF.set_Data('.prog_states.txt', 'file_state', 2)
                drF.a_data_dRap('\n' + str(daF.set_Act_Date()))
                drF.a_data_dRap('\t\t' + scomm)
                drF.dailyRap(textfeldday)


def items_selected(event):
    selected_indices = listbox.curselection()  # get selected indices
    selected_comms = ",".join([listbox.get(index1) for index1 in selected_indices])  # get selected items
    msg = f'Wollen Sie: {selected_comms} auswählen?'
    select_Com(msg, selected_comms)


def openFile():
    tf = filedialog.askopenfilename(
        initialdir="/home/peti/Projects/OpenWtTaker",
        title="Open Text file",
        filetypes=(("Text Files", "*.*"),),
    )
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    textfeldweek.insert(END, data)
    tf.close()


def check_Tb_State():
    work_state = daF.get_int_Data('.prog_states.txt', 'work_state')
    if work_state == 0:
        timebut_text.set('Start')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 12), background='green', foreground='black')
    else:
        timebut_text.set('Stop')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 12), background='red', foreground='black')


def check_User_State():
    user_state = daF.get_int_Data('.prog_states.txt', 'user_state')
    if user_state == 0:
        mbox.showinfo('Achtung', 'Kein User registriert.\n'
                                 'User registrieren')
        seU.create_User_Set_Win(main_window)
    daF.set_Data('.prog_states.txt', 'prog_state', 1)


def checkProgStat():
    progState = daF.get_int_Data('.prog_states.txt', 'prog_state')
    filestate = daF.get_int_Data('.prog_states.txt', 'file_state')
    if progState == 1:
        if filestate == 0:
            drF.write_titelDrap()
            daF.set_Data('.prog_states.txt', 'file_state', 1)
            drF.dailyRap(textfeldday)
        else:
            drF.dailyRap(textfeldday)


################################################################################
# Main Window start
################################################################################

main_window = tk.Tk()
main_window.title("Open Worktime Tracker")
main_window.geometry('790x510')
main_window.minsize(width=790, height=565)
bgstate = 0
dark_grey = '#2b2b2b'  # darkgrey
light_grey = '#5c5c5c'  # lightgrey

main_window.configure(bg=dark_grey)

# variables
timebut_text = tk.StringVar()
u_name = tk.StringVar(value=daF.get_str_Data('user_hpf.txt', 'u_name'))
u_prename = tk.StringVar(value=daF.get_str_Data('user_hpf.txt', 'u_prename'))
u_number = tk.StringVar(value=daF.get_str_Data('user_hpf.txt', 'u_number'))
comm_list = daF.read_List('temp/.list_commisions.txt')
comm_list_var = tk.StringVar(value=comm_list)
bg_col_stat = tk.StringVar(value='Light')
act_date = tk.StringVar(value=daF.get_Act_Date())
# Pictures
logo = tk.PhotoImage(file='/home/peti/Projects/OpenWtTaker/picture/logo_001.png')
notepic = tk.PhotoImage(file='/home/peti/Projects/OpenWtTaker/picture/note_bg.png')

# Styles
style_L_small = ttk.Style()
style_L_small.configure("SL.TLabel", font=('Calibri', 14), background=dark_grey, foreground=light_grey)
style_titel = ttk.Style()
style_titel.configure("tS.TLabel", font=('Calibri', 20), background=dark_grey, foreground=light_grey)
style_B_small = ttk.Style()
style_B_small.configure("bstyle.TButton", font=('Calibri', 12), background=dark_grey, foreground=light_grey)
style_notebook = ttk.Style()
style_notebook.configure("BW.TLabel", background=dark_grey, foreground=light_grey)
style_On_Off = ttk.Style()
style_On_Off.configure("onOff.TButton", font=('Calibri', 12), background='green', foreground=dark_grey)
style_raster_hor = ttk.Style()
style_raster_hor.configure("rSh.TLabel", background=dark_grey, width=2)
style_raster_ver = ttk.Style()
style_raster_ver.configure("rSv.TLabel", background=dark_grey, width=25)

# notebook
notebook = ttk.Notebook(main_window, style="BW.TLabel")
notebook.grid(row=0, column=0)
fdRap = ttk.Frame(notebook, style="BW.TLabel")
fwRap = ttk.Frame(notebook, style="BW.TLabel")
fComm = ttk.Frame(notebook, style="BW.TLabel")
fSett = ttk.Frame(notebook, style="BW.TLabel")
fr_ferien = ttk.Frame(notebook, style="BW.TLabel")

# Notebook Frames erstellen mit Logo und Titel
frameList = [fdRap, fwRap, fComm, fSett, fr_ferien]
note_list = ['Tagesrapport', 'Wochenrapport', 'Kommission', 'Einstellungen', 'Ferien']
for i in range(len(frameList)):
    notebook.add(frameList[i], text=note_list[i], image=notepic, compound='center')
    laF.Labels.label_Logo(frameList[i], logo, "BW.TLabel")
    laF.Labels.label_Titel(frameList[i], note_list[i], "tS.TLabel")
    raF.Raster.rasterVert(frameList[i], "rSv.TLabel")
    raF.Raster.rasterHor(frameList[i], "rSh.TLabel")

###########################################################
# TagesrapportSeite
###########################################################
meF.menutaskbar(main_window, dark_grey, light_grey, openFile)

# Uhr
labelUhr = ttk.Label(fdRap, style="SL.TLabel")
labelUhr.grid(row=2, column=3, sticky='nw')
zeit = ''
ttk.Label(fdRap, textvariable=act_date, style="SL.TLabel").grid(row=1, column=3, sticky='sw')

# Mitarbeiter Label erstellen
label_list = ["Mitarbeiter Nr.", "Name", "Vorname", "", "Kommission"]
for index in range(len(label_list)):
    laF.Labels.label_Small(fdRap, label_list[index], "SL.TLabel", index + 4, 1)
user_list = [u_number, u_name, u_prename]
for i in range(len(user_list)):
    laF.Labels.label_Interact(fdRap, user_list[i], "SL.TLabel", i + 4, 2)

listbox = Listbox(fdRap, listvariable=comm_list_var, height=10, selectmode='browse')
listbox.grid(row=9, column=1, padx=5, rowspan=7, sticky='W')
listbox.bind('<<ListboxSelect>>', items_selected)

textfeldday = Text(fdRap, height=10, width=65)
textfeldday.grid(row=9, column=2, rowspan=7, columnspan=4, padx=5, sticky='W')

buF.Buttons.time_button(fdRap, timebut_text, "onOff.TButton", push_Timebutton)
################################################################################
# Wochenrapportseite
################################################################################
textfeldweek = Text(fwRap, width=92, height=18)
textfeldweek.grid(row=4, column=1, padx=5)
buF.Buttons.com_button(fwRap, 'Wochenrapport', notepic, "bstyle.TButton", wrF.weeklyRap(textfeldweek), 3, 1)

################################################################################
# Kommissionsseite
################################################################################
comm_det_lab = ['Kom.Nr.', 'Adresse', 'Ort/Plz']
laF.Labels.label_Titel(fComm, 'Aktuelle Kommission', "tS.TLabel")
for num in range(3):
    laF.Labels.label_Small(fComm, comm_det_lab[num], "SL.TLabel", num + 3, 1)

################################################################################
# Einstellungsseite
################################################################################
dat_name_l = ['Programm          ',
              'Daten löschen     ',
              'User löschen      ',
              'Werkszustand      ']
dat_func_l = [syS.reset_Stats, syS.delete_Data, syS.reset_User, syS.reset_All]
laF.Labels.label_Small(fSett, 'Styling ändern    ', "SL.TLabel", 7, 1)
buF.Buttons.com_button_interact(fSett, bg_col_stat, notepic, "bstyle.TButton", changeBackground, 7, 2)

buF.Buttons.com_button(fSett, 'Userdaten ändern  ', notepic, "bstyle.TButton",
                       lambda: seU.create_User_Set_Win(main_window), 12, 2)
for i in range(len(dat_name_l)):
    laF.Labels.label_Small(fSett, dat_name_l[i], "SL.TLabel", i + 8, 1)
    buF.Buttons.com_button(fSett, dat_name_l[i], notepic, "bstyle.TButton", dat_func_l[i], i + 8, 2)

tick()
check_Tb_State()
check_User_State()
checkProgStat()
main_window.mainloop()
