from tkinter import ttk


class Labels:
    def __init__(self, l_text, l_font, l_bg, l_fg, l_row, l_col, l_pic):
        self.t = l_text
        self.fo = l_font
        self.b = l_bg
        self.f = l_fg
        self.r = l_row
        self.c = l_col
        self.p = l_pic

    def label_Small(self, l_text, l_style, l_row, l_col):
        ttk.Label(self, text=l_text, style=l_style). \
            grid(row=l_row, column=l_col, padx=5, sticky='W')

    def label_Interact(self, l_text, s, r, c):
        ttk.Label(self, textvariable=l_text, style=s). \
            grid(row=r, column=c, padx=5, sticky='W')

    def label_Titel(self, t, s):
        ttk.Label(self, text=t, style=s). \
            grid(row=2, column=1, columnspan=3, padx=5,
                 sticky='W')

    def label_Pics(self, p, s):
        ttk.Label(self, image=p, style=s).grid(row=1, column=1, columnspan=2)
