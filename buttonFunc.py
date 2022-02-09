from tkinter import ttk


class Buttons:
    def __init__(self, b):
        self.b_bg = b

    def com_button(self, t, p, s, com, r, c):
        ttk.Button(self, text=t, image=p, style=s, command=com, compound='center').grid(row=r, column=c)

    def com_button_interact(self, t, p, s, com, r, c):
        ttk.Button(self, textvariable=t, image=p, style=s, command=com, compound='center').grid(row=r, column=c)

    def time_button(self, t, s, com):
        ttk.Button(self, textvariable=t, style=s,
                   command=com).grid(row=17, column=4)
