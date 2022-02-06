import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
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
        buf.Buttons.time_button(fdRap, but_state, "bstyle.TButton", changeStat)
        mef.set_Time()
        textfeldday.insert(INSERT, '\t' + mef.set_Hour() + ':' + mef.set_Min())
    else:
        but_state.set('Start')
        time_but_col = 'green'
        buf.Buttons.time_button(fdRap, but_state, "bstyle.TButton", changeStat)
        textfeldday.insert(INSERT, ' - ' + mef.set_Hour() + ':' + mef.set_Min() + '\t')
        #        result = woc.worktime_calc()
        textfeldday.insert(INSERT, '\t' + woc.worktime_calc() + '\n')
        mef.set_Time()
    but_state_count += 1


def changeBackground():
    global bgstate
    if bgstate % 2 == 0:
        main_window.config(bg=light_grey)
        stylenotebook.configure("BW.TLabel", background=light_grey, foreground=dark_grey)
        styleLabel.configure("SL.TLabel", font=('Calibri', 20), background=light_grey, foreground=dark_grey)
        buttonstyle.configure("bstyle.TButton", font=('Calibri', 16), background=light_grey, foreground=dark_grey)
        men.menutaskbar(main_window, light_grey, dark_grey)
        bg_col_stat.set('Dark')
        bgstate += 1
    else:
        main_window.config(bg=dark_grey)
        stylenotebook.configure("BW.TLabel", background=dark_grey, foreground=light_grey)
        styleLabel.configure("SL.TLabel", font=('Calibri', 20), background=dark_grey, foreground=light_grey)
        buttonstyle.configure("bstyle.TButton", font=('Calibri', 16), background=dark_grey, foreground=light_grey)
        men.menutaskbar(main_window, dark_grey, light_grey)
        bg_col_stat.set('Light')
        bgstate += 1


def askYesNo(msg, scomm):
    reply = mbox.askyesno('Bestätigen', msg)
    if reply:
        textfeldday.insert(END, scomm + ': ')
        textfeldday.insert(INSERT, mef.set_Date())


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


global_state = 0
but_state_count = 0
bgstate = 0
time_but_col = 'green'
dark_grey = '#2b2b2b'  # darkgrey
light_grey = '#5c5c5c'  # lightgrey

# Main Window start
main_window = tk.Tk()
main_window.title("Open Worktime Tracker")
main_window.geometry('800x550')
main_window.minsize(width=800, height=550)
main_window.configure(bg=dark_grey)

# Pictures
logo = tk.PhotoImage(file='logo_002.2.png')
pdRap = tk.PhotoImage(file='pdRap.png')
pwRap = tk.PhotoImage(file='pwRap.png')
pComm = tk.PhotoImage(file='pCom.png')

# Styles
styleLabel = ttk.Style()
styleLabel.configure("SL.TLabel", font=('Calibri', 20), background=dark_grey, foreground=light_grey)
buttonstyle = ttk.Style()
buttonstyle.configure("bstyle.TButton", font=('Calibri', 16), background=dark_grey, foreground=light_grey)
stylenotebook = ttk.Style()
stylenotebook.configure("BW.TLabel", background=dark_grey, foreground=light_grey)

# notebook
notebook = ttk.Notebook(main_window, style="BW.TLabel")
notebook.grid(row=0, column=0)
fdRap = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fwRap = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fComm = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")
fSett = ttk.Frame(notebook, width=920, height=500, style="BW.TLabel")

# NB Seiten erstellen
frameList = [fdRap, fwRap, fComm, fSett]
label_list = ["Mitarbeiter", "Name", "Vorname", "Baustelle:", "Aktueller Tag:", "Light/Dark"]
note_list = ['Tagesrapport', 'Wochenrapport', 'Kommission', 'Einstellungen']
for index in range(len(frameList)):
    laf.Labels.label_Pics(frameList[index], logo, "BW.TLabel")
    frameList[index].grid()
    notebook.add(frameList[index], text=note_list[index], image=pwRap, compound='center')
    laf.Labels.label_Titel(frameList[index], note_list[index], "SL.TLabel")
    raF.Raster.rasterCompl(frameList[index], "BW.TLabel")
    laf.Labels.label_Small(fdRap, label_list[index], "SL.TLabel", index + 4, 1)

# variables
but_state = tk.StringVar()
but_state.set('Start')
name = tk.StringVar()
name.set('Flütsch')
prename = tk.StringVar()
prename.set('Hanspeter')
comm_list = 'Adliswil', 'Bettlach', 'Aarau', 'Schöftland', 'Bulle', 'Lausanne'
comm_list_var = tk.StringVar()
comm_list_var.set(comm_list)
bg_col_stat = tk.StringVar()
bg_col_stat.set('Dark')

# TagesrapportSeite
men.menutaskbar(main_window, dark_grey, light_grey)
labelUhr = ttk.Label(fdRap, style="SL.TLabel")
labelUhr.grid(row=1, column=4, sticky='N')
zeit = ''
laf.Labels.label_Interact(fdRap, name, "SL.TLabel", 5, 2)
laf.Labels.label_Interact(fdRap, prename, "SL.TLabel", 6, 2)
laf.Labels.label_h_Left(fdRap, "Aktueller Tag:", "SL.TLabel", 8, 3)
listbox = Listbox(fdRap, listvariable=comm_list_var, height=10, selectmode='browse')
listbox.grid(row=7, column=1, padx=5, sticky='W')
textfeldday = Text(fdRap, height=10, width=75)
textfeldday.grid(row=7, column=2, columnspan=3, padx=5, sticky='W')
buf.Buttons.time_button(fdRap, but_state, "bstyle.TButton", changeStat)
listbox.bind('<<ListboxSelect>>', items_selected)

# Wochenrapportseite
fo_but = ttk.Button(fwRap, text='File open', style="bstyle.TButton", command=openFile)
fo_but.grid(row=1, column=3, sticky='E')
pathh = Entry(fwRap)
pathh.grid(row=1, column=4, sticky='W')
textfeldweek = Text(fwRap, width=100, height=25)
textfeldweek.grid(row=3, column=1, columnspan=4, rowspan=10)

# Kommissionsseite
comm_det_lab = ['Kom.Nr.', 'Adresse', 'Ort/Plz']
for num in range(3):
    laf.Labels.label_Small(fComm, comm_det_lab[num], "SL.TLabel", num + 3, 1)

# Einstellungsseite
buf.Buttons.com_button_interact(fSett, bg_col_stat, "bstyle.TButton", changeBackground, 7, 1)

tick()
main_window.mainloop()
