from tkinter import ttk


def label_small(win, l_text, l_style, l_row, l_col):
    ttk.Label(win, text=l_text, style=l_style). \
        grid(row=l_row, column=l_col, padx=5, sticky='W')


def label_interact(win, l_text, s, r, c):
    ttk.Label(win, textvariable=l_text, style=s). \
        grid(row=r, column=c, padx=5, sticky='W')


def label_titel(win, t, s):
    ttk.Label(win, text=t, style=s). \
        grid(row=2, column=1, padx=5, sticky='W')


def label_logo(win, p, s):
    ttk.Label(win, image=p, style=s).grid(row=1, column=1,
                                          columnspan=2,
                                          sticky='W')
