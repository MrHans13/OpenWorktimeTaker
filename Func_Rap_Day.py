from tkinter import INSERT
import Func_Data as daF

drap = daF.get_str_path('drap')


def write_daily_tf(textfeldday):
    datei = open(drap, "r")
    textfeldday.delete("1.0", "end")
    for zeile in datei:
        textfeldday.insert(INSERT, zeile)


def write_titel_drap():
    f = open(drap, 'w')
    f.write("Datum:\t\tCommission:\t\tStart:\tStop:\tZeit:\tÜ-Zeit:\n")
    f.close()


def a_data_drap(msg):
    f = open(drap, 'a')
    f.write(msg)
    f.close()
