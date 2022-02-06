import tkinter as tk
from tkinter import ttk


class Buttons:
    def __init__(self, b):
        self.b_bg = b

    def com_button(self, t, fo, b_bg, f, com, r, c):
        tk.Button(self, text=t, font=fo,
                  bg=b_bg, fg=f, command=com).grid(row=r, column=c)

    def com_button_interact(self, t, s, com, r, c):
        ttk.Button(self, textvariable=t, style=s, command=com).grid(row=r, column=c)

    def c_but_l_act(self, t, fo, b, f, com, r):
        tk.Button(self, textvariable=t, font=fo,
                  bg=b, fg=f,
                  width=10, command=com).grid(row=r, column=1)

    def c_but_hl_act(self, t, fo, b, f, com, r):
        tk.Button(self, textvariable=t, font=fo,
                  bg=b, fg=f,
                  width=10, command=com).grid(row=r, column=2)

    def c_but_hr_act(self, t, fo, b, f, com, r):
        tk.Button(self, textvariable=t, font=fo,
                  bg=b, fg=f,
                  width=10, command=com).grid(row=r, column=3)

    def c_but_r_act(self, t, fo, b, f, com, r):
        tk.Button(self, textvariable=t, font=fo,
                  bg=b, fg=f,
                  width=10, command=com).grid(row=r, column=3)

    def time_button(self, t, s, com):
        ttk.Button(self, textvariable=t, style=s,
                   command=com).grid(row=8, column=4)
