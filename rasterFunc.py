import tkinter as tk


class Raster:
    def __init__(self, r_bg):
        self.b = r_bg

    def rasterCompl(self, b):
        for i in range(9):
            tk.Label(self, bg=b, width=25).grid(row=0, column=i + 1,
                                                padx=2)
        for i in range(23):
            tk.Label(self, bg=b, width=2,
                     height=2).grid(row=i + 1, column=0,
                                    padx=2, pady=2)
