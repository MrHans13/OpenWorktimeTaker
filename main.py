#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
import measureFunc as mef
import labelFunc as laF
import menuFunc as meF
import tkinter.messagebox as mbox
import buttonFunc as buF
import rasterFunc as raF
import dataFunc as daF
import calcFunc as caF
import printFunc as prF
import setUser as seU
import sys_Setting as syS
import week_R_Func as wrF
import day_R_Func as drF


def tick():
    global zeit
    neuezeit = time.strftime('%H:%M:%S')
    if neuezeit != zeit:
        zeit = neuezeit
        labelUhr.config(text=zeit)
    labelUhr.after(200, tick)


def push_Timebutton():
    work_state = daF.read_Int('.state_work.txt')
    fileState = daF.read_Int('.state_file.txt')
    if work_state == 0:
        if fileState < 1:
            mbox.showinfo('Achtung', 'bitte erst\nKommission auswählen...')
        if 1 <= fileState < 3:
            timebut_text.set('Stop')
            style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)
            mef.set_Start_Time()
            daF.write_Stat_Data('.state_work.txt', '1')
            daF.write_Stat_Data('.state_file.txt', '3')
            prF.print_To_dRap()
            drF.dailyRap(textfeldday)
        if fileState >= 3:
            timebut_text.set('Stop')
            style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)
            mef.set_Start_Time()
            daF.write_Stat_Data('.state_work.txt', '1')
            daF.write_Stat_Data('.state_file.txt', '5')
            prF.print_To_dRap()
            drF.dailyRap(textfeldday)

    else:
        timebut_text.set('Start')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)
        daF.write_Stat_Data('.state_work.txt', '0')
        if fileState < 5:
            daF.write_Stat_Data('.state_file.txt', '4')
        else:
            daF.write_Stat_Data('.state_file.txt', '6')
        mef.set_Stop_Time()
        caF.calc_Work_Time()
        prF.print_To_dRap()

        drF.dailyRap(textfeldday)


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


def askYesNo(msg, scomm):
    reply = mbox.askyesno('Bestätigen', msg)
    if reply:
        fileState = daF.read_Int('.state_file.txt')
        workstate = daF.read_Int('.state_work.txt')
        if workstate == 1:
            mbox.showinfo('Achtung', 'Sie müssen erst Zeit stoppen.\n'
                                     'Kommission wird beim nächsten Start automatisch\n'
                                     'übernommern')
        if fileState < 3:
            daF.write_Stat_Data('.act_com.txt', scomm)
            daF.write_Stat_Data('.state_file.txt', '2')
            daF.write_Stat_Data('.state_week.txt', '1')
            daF.write_Stat_Data('.state_day.txt', '1')
            prF.print_To_dRap()
            drF.dailyRap(textfeldday)
        if fileState >= 3:
            daF.write_Stat_Data('.act_com.txt', scomm)
            daF.write_Stat_Data('.state_file.txt', str(fileState))
            drF.dailyRap(textfeldday)


def items_selected(event):
    selected_indices = listbox.curselection()  # get selected indices
    selected_comms = ",".join([listbox.get(i3) for i3 in selected_indices])  # get selected items
    msg = f'Wollen Sie: {selected_comms} auswählen?'
    daF.write_Stat_Data('.state_file.txt', '1')
    daF.write_Stat_Data('.state_com.txt', '1')
    askYesNo(msg, selected_comms)


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

def restart(root):
    root.destroy()
    root = Tk()
    root.mainloop()

def checkTbutton():
    work_state = daF.read_Int('.state_work.txt')
    if work_state == 0:
        timebut_text.set('Start')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)
    else:
        timebut_text.set('Stop')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)


def check_User_State():
    user_state = daF.read_Int('.state_user.txt')
    mef.set_Date()

    if user_state == 0:
        mbox.showinfo('Achtung', 'Kein User registriert.\n'
                                 'User registrieren')
        seU.create_User_Set_Win(main_window)
        checkProgStat()
    else:
        checkProgStat()


def checkProgStat():
    progState = daF.read_Int('.state_prog.txt')
    if 1 < progState < 2:
        drF.dailyRap(textfeldday)


def check_F_State():
    fileState = daF.read_Int('.state_file.txt')
    if fileState == 0:
        drF.write_titelDrap()
        wrF.write_titelWrap()
        drF.dailyRap(textfeldday)
    if fileState == 1:
        drF.dailyRap(textfeldday)


def check_com_Stat():
    comstat = daF.read_Int('.state_com.txt')


bgstate = 0
dark_grey = '#2b2b2b'  # darkgrey
light_grey = '#5c5c5c'  # lightgrey
################################################################################
# Main Window start
################################################################################

main_window = tk.Tk()
main_window.title("Open Worktime Tracker")
main_window.geometry('790x510')
main_window.minsize(width=790, height=565)

main_window.configure(bg=dark_grey)

# variables
timebut_text = tk.StringVar()
u_name = tk.StringVar(value=daF.r_Str_temp('.user_nr.txt'))
name = tk.StringVar(value=daF.r_Str_temp('.user_name.txt'))
prename = tk.StringVar(value=daF.r_Str_temp('.user_prename.txt'))
comm_list = daF.read_List('.list_commisions.txt')
comm_list_var = tk.StringVar(value=comm_list)
bg_col_stat = tk.StringVar(value='Light')

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
labelUhr.grid(row=1, column=3, sticky='nw')
zeit = ''

# Mitarbeiter Label erstellen
label_list = ["Mitarbeiter Nr.", "Name", "Vorname", "Baustelle"]
for index in range(len(label_list)):
    laF.Labels.label_Small(fdRap, label_list[index], "SL.TLabel", index + 4, 1)
user_list = [u_name, name, prename]
for i in range(len(user_list)):
    laF.Labels.label_Interact(fdRap, user_list[i], "SL.TLabel", i + 4, 2)

listbox = Listbox(fdRap, listvariable=comm_list_var, height=10, selectmode='browse')
listbox.grid(row=8, column=1, padx=5, rowspan=7, sticky='W')
listbox.bind('<<ListboxSelect>>', items_selected)

textfeldday = Text(fdRap, height=10, width=65)
textfeldday.grid(row=8, column=2, rowspan=7, columnspan=4, padx=5, sticky='W')

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
dat_name_l = ['User löschen      ', 'Daten löschen     ',
              'Prog. zurücksetzen', 'Werkszustand      ']
dat_func_l = [syS.reset_User, syS.reset_data(textfeldday), syS.reset_Stats, syS.reset_Factory]
laF.Labels.label_Small(fSett, 'Styling ändern    ', "SL.TLabel", 7, 1)
buF.Buttons.com_button_interact(fSett, bg_col_stat, notepic, "bstyle.TButton", changeBackground, 7, 2)
for i in range(len(dat_name_l)):
    laF.Labels.label_Small(fSett, dat_name_l[i], "SL.TLabel", i + 8, 1)
    buF.Buttons.com_button(fSett, dat_name_l[i], notepic, "bstyle.TButton", dat_func_l[i], i + 8, 2)

checkTbutton()
tick()
check_User_State()
main_window.mainloop()
