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


def tick():
    global zeit
    neuezeit = time.strftime('%H:%M:%S')
    if neuezeit != zeit:
        zeit = neuezeit
        labelUhr.config(text=zeit)
    labelUhr.after(200, tick)


def change_T_B_Stat():
    timeButState = daF.read_Int('.workState.txt')
    fileState = daF.read_Int('.fileState.txt')
    if timeButState == 0:
        if fileState < 2:
            mbox.showinfo('Achtung', 'bitte erst\nKommission auswählen...')
        if 2 <= fileState < 4:
            timebut_text.set('Stop')
            style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)
            mef.set_Start_Time()
            daF.write_Stat_Data('.workState.txt', '1')
            daF.write_Stat_Data('.fileState.txt', '3')
            daF.write_Stat_Data('.workState.txt', '1')
            prF.print_To_dRap()
            dailyRap()
        if fileState >= 4:
            timebut_text.set('Stop')
            style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)
            mef.set_Start_Time()
            daF.write_Stat_Data('.workState.txt', '1')
            daF.write_Stat_Data('.fileState.txt', '5')
            prF.print_To_dRap()
            dailyRap()

    else:
        timebut_text.set('Start')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)
        daF.write_Stat_Data('.workState.txt', '0')
        if fileState < 5:
            daF.write_Stat_Data('.fileState.txt', '4')
        else:
            daF.write_Stat_Data('.fileState.txt', '6')
        mef.set_Stop_Time()
        caF.calc_Work_Time()
        prF.print_To_dRap()

        dailyRap()


def dailyRap():
    datei = open("DailyRapport.txt", "r")
    textfeldday.delete("1.0", "end")
    for zeile in datei:
        textfeldday.insert(INSERT, zeile)


def weeklyRap():
    datei = open("WeeklyRapport.txt", "r")
    for zeile in datei:
        textfeldweek.insert(INSERT, zeile)


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
        fileState = daF.read_Int('.fileState.txt')
        workstate = daF.read_Int('.workState.txt')
        if workstate == 1:
            mbox.showinfo('Achtung', 'Sie müssen erst Zeit stoppen.\n'
                                     'Kommission wird beim nächsten Start automatisch\n'
                                     'übernommern')

        if fileState < 3:
            daF.write_Stat_Data('.comm.txt', scomm)
            daF.write_Stat_Data('.fileState.txt', '2')
            daF.write_Stat_Data('.weekState.txt', '1')
            daF.write_Stat_Data('.dayState.txt', '1')
            prF.print_To_dRap()
            dailyRap()
        if fileState >= 3:
            daF.write_Stat_Data('.comm.txt', scomm)
            daF.write_Stat_Data('.fileState.txt', str(fileState))
            dailyRap()


def items_selected(event):
    selected_indices = listbox.curselection()  # get selected indices
    selected_comms = ",".join([listbox.get(i3) for i3 in selected_indices])  # get selected items
    msg = f'Wollen Sie: {selected_comms} auswählen?'
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


def checkTbutton():
    timeButState = daF.read_Int('.workState.txt')
    if timeButState == 0:
        timebut_text.set('Start')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)
    else:
        timebut_text.set('Stop')
        style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)


def checkProgStat():
    user_state = daF.read_Int('.userState.txt')
    progState = daF.read_Int('.progState.txt')
    if user_state == 0:
        mbox.showinfo('Achtung', 'Kein User registriert.\n'
                                 'User registrieren')
        seU.create_User_Set_Win(main_window)
    if progState == 0:
        name.set(daF.read_Str('.name.txt'))
        prename.set(daF.read_Str('.prename.txt'))
        mef.set_Date()
        daF.write_titelWrap()
        daF.write_titelDrap()
        daF.write_Stat_Data('.progState.txt', '1')
        daF.write_Stat_Data('.fileState.txt', '1')
        dailyRap()


bgstate = 0
dark_grey = '#2b2b2b'  # darkgrey
light_grey = '#5c5c5c'  # lightgrey

# Main Window start
main_window = tk.Tk()
main_window.title("Open Worktime Tracker")
main_window.geometry('850x550')
main_window.minsize(width=800, height=550)
main_window.configure(bg=dark_grey)

# variables
timebut_text = tk.StringVar()
name = tk.StringVar()
name.set(daF.read_Str('.name.txt'))
prename = tk.StringVar()
prename.set(daF.read_Str('.prename.txt'))
comm_list_file = open('commision_file.txt', 'r')
comm_list = comm_list_file.read().split()
comm_list_file.close()
comm_list_var = tk.StringVar()
comm_list_var.set(comm_list)
bg_col_stat = tk.StringVar()
bg_col_stat.set('Light')

# Pictures
logo = tk.PhotoImage(file='logo_001.png')
notepic = tk.PhotoImage(file='note_bg.png')

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
style_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)
style_raster_hor = ttk.Style()
style_raster_hor.configure("rSh.TLabel", background=dark_grey, width=2)
style_raster_ver = ttk.Style()
style_raster_ver.configure("rSv.TLabel", background=dark_grey, width=25)
# notebook
notebook = ttk.Notebook(main_window, style="BW.TLabel")
notebook.grid(row=0, column=0)
fdRap = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fwRap = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fComm = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fSett = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fr_ferien = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")

# Notebook Frames erstellen mit Logo und Titel
frameList = [fdRap, fwRap, fComm, fSett, fr_ferien]
note_list = ['Tagesrapport', 'Wochenrapport', 'Kommission', 'Einstellungen', 'Ferien']
for i in range(len(frameList)):
    notebook.add(frameList[i], text=note_list[i], image=notepic, compound='center')
    laF.Labels.label_Logo(frameList[i], logo, "BW.TLabel")
    laF.Labels.label_Titel(frameList[i], note_list[i], "tS.TLabel")

for index in range(len(frameList)):
    raF.Raster.rasterVert(frameList[index], "rSv.TLabel")
    raF.Raster.rasterHor(frameList[index], "rSh.TLabel")

# TagesrapportSeite
meF.menutaskbar(main_window, dark_grey, light_grey, openFile)

# Uhr
labelUhr = ttk.Label(fdRap, style="SL.TLabel")
labelUhr.grid(row=1, column=5)
zeit = ''

# Mitarbeiter Label erstellen
label_list = ["Mitarbeiter Nr.", "Name", "Vorname", "Baustelle"]
for index in range(len(label_list)):
    laF.Labels.label_Small(fdRap, label_list[index], "SL.TLabel", index + 4, 1)
laF.Labels.label_Interact(fdRap, name, "SL.TLabel", 7, 2)
laF.Labels.label_Interact(fdRap, prename, "SL.TLabel", 8, 2)
listbox = Listbox(fdRap, listvariable=comm_list_var, height=10, selectmode='browse')
listbox.grid(row=10, column=1, padx=5, rowspan=7, sticky='W')
textfeldday = Text(fdRap, height=10, width=70)
textfeldday.grid(row=10, column=2, rowspan=7, columnspan=4, padx=5, sticky='W')
buF.Buttons.time_button(fdRap, timebut_text, "onOff.TButton", change_T_B_Stat)
listbox.bind('<<ListboxSelect>>', items_selected)

# Wochenrapportseite
textfeldweek = Text(fwRap, width=70, height=15)
textfeldweek.grid(row=3, column=1, padx=5, rowspan=20, columnspan=3)

# Kommissionsseite
comm_det_lab = ['Kom.Nr.', 'Adresse', 'Ort/Plz']
laF.Labels.label_Titel(fComm, 'Aktuelle Kommission', "tS.TLabel")
for num in range(3):
    laF.Labels.label_Small(fComm, comm_det_lab[num], "SL.TLabel", num + 3, 1)

# Einstellungsseite
laF.Labels.label_Small(fSett, 'Styling ändern', "SL.TLabel", 7, 1)
laF.Labels.label_Small(fSett, 'Werkszustand  ', "SL.TLabel", 12, 1)
buF.Buttons.com_button_interact(fSett, bg_col_stat, notepic, "bstyle.TButton", changeBackground, 7, 2)
buF.Buttons.com_button(fSett, 'Werkszustand', notepic, "bstyle.TButton", prF.factory_Reset, 12, 2)

checkTbutton()
checkProgStat()
tick()
main_window.mainloop()
