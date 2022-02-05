import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self):
        super().__init__()
        # root Window
        self.style = ttk.Style(self)
        # initialize the notebook
        notebook = ttk.Notebook(self)
        fdRap = tk.Frame(notebook)
        fwRap = tk.Frame(notebook)
        fComm = tk.Frame(notebook)
        fSett = tk.Frame(notebook)
        fdRap.grid()
        fwRap.grid()
        fComm.grid()
        fSett.grid()
        notebook.add(fdRap, text='Tagesrapport:')
        notebook.add(fwRap, text='Wochenrapport:')
        notebook.add(fComm, text='Kommission:')
        notebook.add(fSett, text='Einstellungen:')

        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=3, padx=10, pady=10,  sticky='w')
        # button
        btn = ttk.Button(self, text='Show')
        btn.grid(column=2, row=3, padx=10, pady=10,  sticky='w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    logo = tk.PhotoImage(file='logo.png')
    app.mainloop(root)
