from tkinter import *


def menutaskbar(win, b, f, c1):
    menubar = Menu(win, bg=b, fg=f, relief='flat')
    win.config(menu=menubar)
    file_menu = Menu(menubar)
    conf_menu = Menu(menubar)
    menubar.add_cascade(label="File",
                        menu=file_menu)
    file_menu.add_command(label='Open',
                          command=c1)
    file_menu.add_command(label='Quit',
                          command=win.destroy)
