import tkinter as tk


class Buttons:
    def __init__(self, t, fo, b, f, r, c):
        self.b_text = t
        self.b_font = fo
        self.b_bg = b
        self.b_fg = f
        self.b_row = r
        self.b_column = c

    def com_button(self, t, fo, b, f, com, r, c):
        tk.Button(self, text=t, font=fo,
                  bg=b, fg=f, command=com).grid(row=r, column=c)

    def com_button_interact(self, t, fo, b, f, com, r, c):
        tk.Button(self, textvariable=t, font=fo,
                  bg=b, fg=f,
                  width=10, command=com).grid(row=r, column=c)

    def com_button_left_interact(self, t, fo, b, f, com, r, c):
        tk.Button(self, textvariable=t, font=fo,
                  bg=b, fg=f,
                  width=10, command=com).grid(row=r, column=c, sticky='w')

    def time_button(self, t, fo, b, f, com):
        tk.Button(self, textvariable=t, font=fo,
                  bg=b, fg=f,
                  width=10, height=2, command=com).grid(row=7, column=4)
