import tkinter as tk
from tkinter import ttk

class Raster:
    def __init__(self, r_bg):
        self.b = r_bg

    def rasterCompl(self, b):
        for i in range(9):
            ttk.Label(self, style=b).grid(row=0, column=i + 1,
                                                padx=2)
        for i in range(23):
            ttk.Label(self, style=b).grid(row=i + 1, column=0,
                                    padx=2, pady=2)

    def rasterTtk(self, l_text, l_style):
        for i4 in range(9):
            ttk.Label(self, text=l_text, style=l_style).grid(row=1, column=i4 + 1)
        for i5 in range(20):
            ttk.Label(self, text=l_text, style=l_style).grid(row=i5+1, column=1)