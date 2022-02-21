from tkinter import ttk


def raster_vert(self, b):
    for i in range(9):
        ttk.Label(self, style=b).grid(row=0, column=i + 1,
                                      padx=2)


def raster_hor(self, b):
    for i in range(23):
        ttk.Label(self, style=b).grid(row=i + 1, column=0, pady=5)
