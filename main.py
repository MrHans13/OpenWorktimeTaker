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
            styleLabel.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)
            mef.set_Start_Time()
            daF.write_Stat_Data('.workState.txt', '1')
            daF.write_Stat_Data('.fileState.txt', '3')
            daF.write_Stat_Data('.workState.txt', '1')
            prF.print_To_dRap()
            dailyRap()
        if fileState >= 4:
            timebut_text.set('Stop')
            styleLabel.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)
            mef.set_Start_Time()
            daF.write_Stat_Data('.workState.txt', '1')
            daF.write_Stat_Data('.fileState.txt', '5')
            prF.print_To_dRap()
            dailyRap()

    else:
        timebut_text.set('Start')
        styleLabel.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)
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
        stylenotebook.configure("BW.TLabel", background=light_grey, foreground=dark_grey)
        styleLabel.configure("SL.TLabel", font=('Calibri', 20), background=light_grey, foreground=dark_grey)
        buttonstyle.configure("bstyle.TButton", font=('Calibri', 12), background=dark_grey, foreground=light_grey)
        meF.menutaskbar(main_window, light_grey, dark_grey)
        bg_col_stat.set('Dark')
        bgstate += 1
    else:
        main_window.config(bg=dark_grey)
        stylenotebook.configure("BW.TLabel", background=dark_grey, foreground=dark_grey)
        styleLabel.configure("SL.TLabel", font=('Calibri', 20), background=dark_grey, foreground=light_grey)
        buttonstyle.configure("bstyle.TButton", font=('Calibri', 12), background=dark_grey, foreground=light_grey)
        meF.menutaskbar(main_window, dark_grey, light_grey)
        bg_col_stat.set('Light')
        bgstate += 1


def askYesNo(msg, scomm):
    reply = mbox.askyesno('Bestätigen', msg)
    if reply:
        daF.write_Stat_Data('.comm.txt', scomm)
        daF.write_Stat_Data('.fileState.txt', '2')
        daF.write_Stat_Data('.weekState.txt', '1')
        daF.write_Stat_Data('.dayState.txt', '1')
        prF.print_To_dRap()
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
        filetypes=(("Text Files", "*.*"),)
    )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    textfeldweek.insert(END, data)
    tf.close()


def checkTbutton():
    timeButState = daF.read_Int('.workState.txt')
    if timeButState == 0:
        timebut_text.set('Start')
        styleLabel.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)
    else:
        timebut_text.set('Stop')
        styleLabel.configure("onOff.TButton", font=('Calibri', 18), background='red', foreground=dark_grey)


def checkProgStat():
    progState = daF.read_Int('.progState.txt')

    if progState == 0:
        mef.set_Date()
        daF.write_titelWrap()
        daF.write_titelDrap()
        daF.write_Stat_Data('.progState.txt', '1')
        daF.write_Stat_Data('.fileState.txt', '1')
        dailyRap()
    if progState > 0:
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
name.set('Flütsch')
prename = tk.StringVar()
prename.set('Hanspeter')
comm_list_file = open('commision_file.txt', 'r')
comm_list = comm_list_file.read().split()
comm_list_file.close()
comm_list_var = tk.StringVar()
comm_list_var.set(comm_list)
bg_col_stat = tk.StringVar()
bg_col_stat.set('Dark')

# Pictures
logo = tk.PhotoImage(file='logo_002.1.png')
notepic = tk.PhotoImage(file='note_bg.png')

# Styles
styleLabel = ttk.Style()
styleLabel.configure("SL.TLabel", font=('Calibri', 16), background=dark_grey, foreground=light_grey)
titelStyle = ttk.Style()
titelStyle.configure("tS.TLabel", font=('Calibri', 20), background=dark_grey, foreground=light_grey)
buttonstyle = ttk.Style()
buttonstyle.configure("bstyle.TButton", font=('Calibri', 12), background=dark_grey, foreground=light_grey)
stylenotebook = ttk.Style()
stylenotebook.configure("BW.TLabel", background=dark_grey, foreground=light_grey)
sty_On_Off = ttk.Style()
sty_On_Off.configure("onOff.TButton", font=('Calibri', 18), background='green', foreground=dark_grey)

# notebook
notebook = ttk.Notebook(main_window, style="BW.TLabel")
notebook.grid(row=0, column=0)
fdRap = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fwRap = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fComm = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fSett = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fr_ferien = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")

# NB Seiten erstellen
frameList = [fdRap, fwRap, fComm, fSett, fr_ferien]
label_list = ["Mitarbeiter", "Name", "Vorname", "Baustelle:"]
note_list = ['Tagesrapport', 'Wochenrapport', 'Kommission', 'Einstellungen', 'Ferien']
for index in range(len(frameList)):
    laF.Labels.label_Pics(frameList[index], logo, "BW.TLabel")
    notebook.add(frameList[index], text=note_list[index], image=notepic, compound='center')
    laF.Labels.label_Titel(frameList[index], note_list[index], "tS.TLabel")
    raF.Raster.rasterCompl(frameList[index], "BW.TLabel")
for index in range(len(label_list)):
    laF.Labels.label_Small(fdRap, label_list[index], "SL.TLabel", index + 4, 1)

# TagesrapportSeite
meF.menutaskbar(main_window, dark_grey, light_grey)
labelUhr = ttk.Label(fdRap, style="SL.TLabel")
labelUhr.grid(row=1, column=4, sticky='N')
zeit = ''
laF.Labels.label_Interact(fdRap, name, "SL.TLabel", 5, 2)
laF.Labels.label_Interact(fdRap, prename, "SL.TLabel", 6, 2)
listbox = Listbox(fdRap, listvariable=comm_list_var, height=10, selectmode='browse')
listbox.grid(row=8, column=1, padx=5, sticky='W')
textfeldday = Text(fdRap, height=10, width=75)
textfeldday.grid(row=8, column=2, columnspan=3, padx=5, sticky='W')
buF.Buttons.time_button(fdRap, timebut_text, "onOff.TButton", change_T_B_Stat)
listbox.bind('<<ListboxSelect>>', items_selected)

# Wochenrapportseite
fo_but = ttk.Button(fwRap, text='File open', image=notepic, style="bstyle.TButton", command=openFile, compound='center')
fo_but.grid(row=1, column=3, sticky='E')
pathh = Entry(fwRap)
pathh.grid(row=1, column=4, sticky='W')
textfeldweek = Text(fwRap, width=100, height=25)
textfeldweek.grid(row=3, column=1, columnspan=4, rowspan=10)

# Kommissionsseite
comm_det_lab = ['Kom.Nr.', 'Adresse', 'Ort/Plz']
laF.Labels.label_Titel(fComm, 'Aktuelle Kommission:', "tS.TLabel")
for num in range(3):
    laF.Labels.label_Small(fComm, comm_det_lab[num], "SL.TLabel", num + 3, 1)

# Einstellungsseite
laF.Labels.label_Small(fSett, 'Styling ändern:', "SL.TLabel", 7, 1)
laF.Labels.label_Small(fSett, 'Werkszustand herstellen:', "SL.TLabel", 12, 1)
buF.Buttons.com_button_interact(fSett, bg_col_stat, notepic, "bstyle.TButton", changeBackground, 7, 2)
buF.Buttons.com_button(fSett, 'Werkszustand', notepic, "bstyle.TButton", prF.factory_Reset, 12, 2)

checkTbutton()
checkProgStat()
tick()
main_window.mainloop()
