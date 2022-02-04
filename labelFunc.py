import tkinter as tk


class Labels:
    def __init__(self, l_text, l_font, l_bg, l_fg, l_row, l_col, l_pic):
        self.t = l_text
        self.fo = l_font
        self.b = l_bg
        self.f = l_fg
        self.r = l_row
        self.c = l_col
        self.p = l_pic

    def label_Small(self, t, b, f, r, c):
        tk.Label(self, text=t, font=('Sans Serif', 12),
                 bg=b, fg=f,
                 width=10).grid(row=r, column=c, padx=5, sticky='w')

    def label_Interact(self, l_text, fo, b, f, r, c):
        tk.Label(self, textvariable=l_text, font=fo, bg=b, fg=f).grid(row=r, column=c, padx=5, sticky='W')

    def label_Titel(self, l_text, b, f):
        tk.Label(self, text=l_text, font=('Sans Serif', 20), bg=b, fg=f).grid(row=1, column=1, columnspan=2, padx=5, sticky='W')


    def label_Pics(self, p, b, r, c):
        tk.Label(self, image=p, bg=b).grid(row=r, column=c, columnspan=2)


def label_View(win, t, fo, b, f, r, c):
    tk.Label(win, text=t, font=fo, bg=b, fg=f, width=15).grid(row=r, column=c, padx=5.4, sticky='W')


def label_h_Left(win, t, fo, b, f, r, c):
    tk.Label(win, text=t, font=fo, bg=b, fg=f).grid(row=r, column=c, padx=5, sticky='W')
