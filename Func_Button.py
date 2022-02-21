from tkinter import ttk


def com_button(win, t, p, s, com, r, c):
    ttk.Button(win, text=t, image=p, style=s, command=com, compound='center').grid(row=r, column=c)


def com_button_interact(win, t, s, com, r, c):
    ttk.Button(win, textvariable=t, style=s, compound='center', command=com).grid(row=r, column=c)


def time_button(win, t, s, com):
    ttk.Button(win, textvariable=t, style=s,
               command=com).grid(row=7, column=4, sticky='W')


