from tkinter import INSERT


def write_daily_tf(textfeldday):
    datei = open("temp/Rap_D.txt", "r")
    textfeldday.delete("1.0", "end")
    for zeile in datei:
        textfeldday.insert(INSERT, zeile)


def write_titel_drap():
    w_data_drap("Datum:\t\tCommission:\t\tStart:\tStop:\tZeit:\tÜ-Zeit:\n")


def a_data_drap(msg):
    f = open('temp/Rap_D.txt', 'a')
    f.write(msg)
    f.close()


def w_data_drap(msg):
    f = open('temp/Rap_D.txt', 'w')
    f.write(msg)
    f.close()
