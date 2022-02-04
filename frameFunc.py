import tkinter as tk


class Frames:
    def __init__(self, f_bg):
        self.b = f_bg

    def frameLeft(self, b):
        tk.Frame(self, bg=b, width=200, height=290, borderwidth=1)\
            .grid(row=2, column=1, rowspan=7)

    def notbookFrame(self, b):
        tk.Frame(self, bg=b, width=920, height=500).grid()