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
    if but_state_count % 2 == 0:
        but_state.set('Stop')
        time_button.config(bg='red', fg='black')
        mef.set_Time()
        textfeld.insert(INSERT, '\t' + mef.set_Hour() + ':' + mef.set_Min())
    else:
        but_state.set('Start')
        time_button.config(bg='green', fg='white')
        textfeld.insert(INSERT, ' - ' + mef.set_Hour() + ':' + mef.set_Min() + '\t')
        #        result = woc.worktime_calc()
        textfeld.insert(INSERT, '\t' + woc.worktime_calc() + '\n')
        mef.set_Time()
    but_state_count += 1


def changeBackground():
    global bgstate
    global dark_grey

    if bgstate % 2 == 0:
        main_window.config(bg=light_grey)
        labelUhr.config(bg=light_grey, fg=dark_grey)
        labelUhr.grid(row=1, column=3, padx=10)
        men.menutaskbar(main_window, light_grey, dark_grey)
        for counter_one in range(8):
            laf.label_View(main_window, "", font_titel, light_grey, dark_grey, 0, counter_one)
        for counter_two in range(4):
            laf.Labels.label_Small(main_window, label_list[counter_two], font_name, light_grey, dark_grey,
                                   counter_two + 1, 0)
        laf.Labels.label_Pics(main_window, logo, light_grey, 0, 1)

        laf.Labels.label_Interact(main_window, name, font_name, light_grey, dark_grey, 2, 1)
        laf.Labels.label_Interact(main_window, prename, font_name, light_grey, dark_grey, 3, 1)
        laf.label_h_Left(main_window, "Aktueller Tag:", font_name, light_grey, dark_grey, 4, 1)
        buf.Buttons.com_button(main_window, 'Light/Dark', font_name, light_grey, dark_grey, changeBackground, 15, 0)

        bgstate += 1
    else:
        main_window.config(bg=dark_grey)
        labelUhr.config(bg=dark_grey, fg=light_grey)
        labelUhr.grid(row=1, column=3, padx=10)
        men.menutaskbar(main_window, dark_grey, light_grey)
        raF.Raster.rasterTop(frame1, dark_grey)
        raF.Raster.rasterSide(frame1, dark_grey)
        for index in range(4):
            laf.Labels.label_Small(main_window, label_list[index], font_name, dark_grey, light_grey, i + 1, 0)
        laf.Labels.label_Pics(main_window, logo, dark_grey, 0, 1)
        laf.Labels.label_Interact(main_window, name, font_name, dark_grey, light_grey, 2, 1)
        laf.Labels.label_Interact(main_window, prename, font_name, dark_grey, light_grey, 3, 1)
        laf.label_h_Left(main_window, "Aktueller Tag:", font_name, dark_grey, light_grey, 4, 1)
        buf.Buttons.com_button(main_window, 'Light/Dark', font_name, dark_grey, light_grey, changeBackground, 15, 0)
        bgstate += 1


def askYesNo(msg, scomm):
    reply = mbox.askyesno('Bestätigen', msg)
    if reply:
        textfeld.insert(END, scomm + ': ')
        textfeld.insert(INSERT, mef.set_Date())


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
main_window.geometry('920x500')
main_window.minsize(width=920, height=500)
main_window.configure(bg=dark_grey)
notebook = ttk.Notebook(main_window)
notebook.grid()

frame1 = tk.Frame(notebook, width=920, height=500)
frame2 = tk.Frame(notebook, width=920, height=500)
frame3 = tk.Frame(notebook, width=920, height=500)
frame1.configure(bg=dark_grey)
frame2.configure(bg=dark_grey)
frame3.configure(bg=dark_grey)
frame1.grid()
frame2.grid()
frame3.grid()

notebook.add(frame1, text='Tagesrapport')
notebook.add(frame2, text='Wochenrapport')
notebook.add(frame3, text='Offerte')
logo = tk.PhotoImage(file='logo.png')
for i in range(8):
    laf.label_View(main_window, "", font_titel, dark_grey, light_grey, 0, i)

but_state = tk.StringVar()
but_state.set('Start')
name = tk.StringVar()
name.set('Flütsch')
prename = tk.StringVar()
prename.set('Hanspeter')
comm_list = 'Adliswil', 'Bettlach', 'Aarau', 'Schöftland', 'Bulle', 'Lausanne'
comm_list_var = tk.StringVar(value=comm_list)

labelUhr = tk.Label(main_window, font=font_name,
                    bg=dark_grey, fg=light_grey)
labelUhr.grid(row=0, column=3, padx=10)
zeit = ''

men.menutaskbar(main_window, dark_grey, light_grey)
laf.Labels.label_Pics(main_window, logo, dark_grey, 0, 1)
for i in range(4):
    laf.Labels.label_Small(main_window, label_list[i], font_name, dark_grey, light_grey, i + 1, 0)

laf.Labels.label_Interact(main_window, name, font_name, dark_grey, light_grey, 2, 1)
laf.Labels.label_Interact(main_window, prename, font_name, dark_grey, light_grey, 3, 1)
laf.label_h_Left(main_window, "Aktueller Tag:", font_name, dark_grey, light_grey, 4, 1)

listbox = Listbox(frame1, listvariable=comm_list_var, height=10, selectmode='browse')
listbox.grid(row=5, column=0, padx=5, sticky='W')

textfeld = Text(main_window, height=10, width=75)
textfeld.grid(row=5, column=1, columnspan=3, padx=5, sticky='W')
buf.Buttons.com_button(main_window, 'Light/Dark', font_name, dark_grey, light_grey, changeBackground, 15, 0)

time_button = tk.Button(main_window, textvariable=but_state, font=font_name, bg=time_but_col, fg=dark_grey, width=10,
                        height=2,
                        command=changeStat)
time_button.grid(row=6, column=3, padx=25)

listbox.bind('<<ListboxSelect>>', items_selected)

tick()
main_window.mainloop()
