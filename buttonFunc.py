import tkinter as tk
class Buttons:
    def __init__(self, win, t, fo, b, f, r, c):
        self.win = win
        self.b_text = t
        self.b_font = fo
        self.b_bg = b
        self.b_fg = f
        self.b_row = r
        self.b_column = c

    def return_Button(win, fo, b, f, p, tar):
        tk.Button(win, text='zurück', font=fo,
                  bg=b, fg=f, width=15,
                  command=lambda: p.show_frame(tar)).grid(row=10, column=4)

    def site_Button(win, t, fo, b, f, p, tar, r, c):
        tk.Button(win, text=t, font=fo,
                  bg=b, fg=f, width=15,
                  command=lambda: p.show_frame(tar)).grid(row=r, column=c)

    def com_button(win, t, fo, b, f, com, r , c):
        tk.Button(win, text=t, font=fo,
                  bg=b, fg=f, command=com).grid(row=r, column=c)
