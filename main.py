import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import measureFunc as mef
import labelFunc as laf
import menuFunc as men
import tkinter.messagebox as mbox
import buttonFunc as buf
import worktimeCalc as woc
import rasterFunc as raF


def tick():
    global zeit
    neuezeit = time.strftime('%H:%M:%S')
    if neuezeit != zeit:
        zeit = neuezeit
        labelUhr.config(text=zeit)
    labelUhr.after(200, tick)


def changeStat():
    global but_state_count
    global time_but_col
    if but_state_count % 2 == 0:
        but_state.set('Stop')
        time_but_col = 'red'
        buf.Buttons.time_button(fdRap, but_state, font_name, time_but_col, dark_grey, changeStat)
        mef.set_Time()
        textfeldday.insert(INSERT, '\t' + mef.set_Hour() + ':' + mef.set_Min())
    else:
        but_state.set('Start')
        time_but_col = 'green'
        buf.Buttons.time_button(fdRap, but_state, font_name, time_but_col, dark_grey, changeStat)
        textfeldday.insert(INSERT, ' - ' + mef.set_Hour() + ':' + mef.set_Min() + '\t')
        #        result = woc.worktime_calc()
        textfeldday.insert(INSERT, '\t' + woc.worktime_calc() + '\n')
        mef.set_Time()
    but_state_count += 1


def changeBackground():
    global bgstate
    global dark_grey
    if bgstate % 2 == 0:
        main_window.config(bg=light_grey)
        raF.Raster.rasterTop(fdRap, light_grey)
        raF.Raster.rasterSide(fdRap, light_grey)
        labelUhr.config(bg=light_grey, fg=dark_grey)
        men.menutaskbar(main_window, light_grey, dark_grey)
        stylenotebook.configure("BW.TLabel", background=light_grey)
        fdRap.configure(bg=light_grey)
        fwRap.configure(bg=light_grey)
        fComm.configure(bg=light_grey)
        bg_col_stat.set('Light')
        for index in range(4):
            laf.Labels.label_Small(fdRap, label_list[index], light_grey, dark_grey, index + 2, 1)
        laf.Labels.label_Pics(fdRap, logo, light_grey, 1, 2)
        laf.Labels.label_Interact(fdRap, name, font_name, light_grey, dark_grey, 3, 2)
        laf.Labels.label_Interact(fdRap, prename, font_name, light_grey, dark_grey, 4, 2)
        laf.label_h_Left(fdRap, "Aktueller Tag:", font_name, light_grey, dark_grey, 5, 2)
        bgstate += 1
    else:
        main_window.config(bg=dark_grey)
        raF.Raster.rasterTop(fdRap, dark_grey)
        raF.Raster.rasterSide(fdRap, dark_grey)
        labelUhr.config(bg=dark_grey, fg=light_grey)
        men.menutaskbar(main_window, dark_grey, light_grey)
        stylenotebook.configure("BW.TLabel", background=dark_grey)
        fdRap.configure(bg=dark_grey)
        fwRap.configure(bg=dark_grey)
        fComm.configure(bg=dark_grey)
        bg_col_stat.set('Dark')
        for index in range(4):
            laf.Labels.label_Small(fdRap, label_list[index], dark_grey, light_grey, index + 2, 1)
        laf.Labels.label_Pics(fdRap, logo, dark_grey, 1, 2)
        laf.Labels.label_Interact(fdRap, name, font_name, dark_grey, light_grey, 3, 2)
        laf.Labels.label_Interact(fdRap, prename, font_name, dark_grey, light_grey, 4, 2)
        laf.label_h_Left(fdRap, "Aktueller Tag:", font_name, dark_grey, light_grey, 5, 2)
        bgstate += 1


def askYesNo(msg, scomm):
    reply = mbox.askyesno('Bestätigen', msg)
    if reply:
        textfeldday.insert(END, scomm + ': ')
        textfeldday.insert(INSERT, mef.set_Date())


def items_selected(event):
    selected_indices = listbox.curselection()  # get selected indices
    selected_comms = ",".join([listbox.get(index) for index in selected_indices])  # get selected items
    msg = f'Wollen Sie: {selected_comms} auswählen?'
    askYesNo(msg, selected_comms)


but_state_count = 0
bgstate = 0
time_but_col = 'green'
dark_grey = '#2b2b2b'  # darkgrey
light_grey = '#5c5c5c'  # lightgrey
font_titel = ('Arial', 20)
font_name = ('Arial', 16)
label_list = ["Mitarbeiter", "Name", "Vorname", "Baustelle:", "Aktueller Tag:", "Light/Dark"]

main_window = tk.Tk()
main_window.title("Take your Worktime")
main_window.geometry('920x550')
main_window.minsize(width=920, height=550)
main_window.configure(bg=dark_grey)
logo = tk.PhotoImage(file='logo.png')
pdRap = tk.PhotoImage(file='pdRap.png')
pwRap = tk.PhotoImage(file='pwRap.png')
pComm = tk.PhotoImage(file='pCom.png')
stylenotebook = ttk.Style()
stylenotebook.configure("BW.TLabel", background=dark_grey)
notebook = ttk.Notebook(main_window, style="BW.TLabel")
notebook.grid(row=0, column=0)
fdRap = tk.Frame(notebook, width=920, height=500)
fwRap = tk.Frame(notebook, width=920, height=500)
fComm = tk.Frame(notebook, width=920, height=500)
fSett = tk.Frame(notebook, width=920, height=500)
frameList = [fdRap, fwRap, fComm, fSett]
for framename in frameList:
    framename.configure(bg=dark_grey)
    framename.grid()
notebook.add(fdRap, text='Tagesrapport:')
notebook.add(fwRap, text='Wochenrapport:')
notebook.add(fComm, text='Kommission:')
notebook.add(fSett, text='Einstellungen:')

but_state = tk.StringVar()
but_state.set('Start')
name = tk.StringVar()
name.set('Flütsch')
prename = tk.StringVar()
prename.set('Hanspeter')
comm_list = 'Adliswil', 'Bettlach', 'Aarau', 'Schöftland', 'Bulle', 'Lausanne'
comm_list_var = tk.StringVar(value=comm_list)
bg_col_stat = tk.StringVar()
bg_col_stat.set('Dark')
# TagesrapportSeite

raF.Raster.rasterTop(fdRap, dark_grey)
raF.Raster.rasterSide(fdRap, dark_grey)
labelUhr = tk.Label(fdRap, font=font_name, bg=dark_grey, fg=light_grey)
labelUhr.grid(row=1, column=4)
zeit = ''
men.menutaskbar(main_window, dark_grey, light_grey)
laf.Labels.label_Pics(fdRap, logo, dark_grey, 1, 2)
for i in range(4):
    laf.Labels.label_Small(fdRap, label_list[i], dark_grey, light_grey, i + 2, 1)
laf.Labels.label_Interact(fdRap, name, font_name, dark_grey, light_grey, 3, 2)
laf.Labels.label_Interact(fdRap, prename, font_name, dark_grey, light_grey, 4, 2)
laf.label_h_Left(fdRap, "Aktueller Tag:", font_name, dark_grey, light_grey, 5, 2)
listbox = Listbox(fdRap, listvariable=comm_list_var, height=10, selectmode='browse')
listbox.grid(row=6, column=1, padx=5, sticky='W')
textfeldday = Text(fdRap, height=10, width=75)
textfeldday.grid(row=6, column=2, columnspan=3, padx=5, sticky='W')
buf.Buttons.time_button(fdRap, but_state, font_name, time_but_col, dark_grey, changeStat)
listbox.bind('<<ListboxSelect>>', items_selected)

# Wochenrapportseite

raF.Raster.rasterTop(fwRap, dark_grey)
raF.Raster.rasterSide(fwRap, dark_grey)
laf.Labels.label_Titel(fwRap, 'Aktueller Wochenrapport:', dark_grey, light_grey)
textfeldweek = Text(fwRap, width=100, height=25)
textfeldweek.grid(row=2, column=1)
# Kommissionsseite
raF.Raster.rasterTop(fComm, dark_grey)
raF.Raster.rasterSide(fComm, dark_grey)
laf.Labels.label_Titel(fComm, 'Komission:', dark_grey, light_grey)
comm_det_lab = ['Kom.Nr.', 'Adresse', 'Ort/Plz']
for num in range(3):
    laf.Labels.label_Small(fComm, comm_det_lab[num], dark_grey, light_grey, num + 2, 1)

# Einstellungsseite
raF.Raster.rasterTop(fSett, dark_grey)
raF.Raster.rasterSide(fSett, dark_grey)
laf.Labels.label_Titel(fSett, 'Einstellungen:', dark_grey, light_grey)
buf.Buttons.com_button_interact(fSett, bg_col_stat, font_name, dark_grey, light_grey, changeBackground, 7, 1)


tick()
main_window.mainloop()
