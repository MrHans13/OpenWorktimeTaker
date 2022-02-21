from tkinter import INSERT


def dailyRap(textfeldday):
    datei = open("temp/Rap_D.txt", "r")
    textfeldday.delete("1.0", "end")
    for zeile in datei:
        textfeldday.insert(INSERT, zeile)


def write_titelDrap():
    w_data_dRap("Datum:\t\tKomission:\t\tStart:\tStop:\tZeit:\tÜ-Zeit:\n")


def a_data_dRap(msg):
    f = open('temp/Rap_D.txt', 'a')
    f.write(msg)
    f.close()


def w_data_dRap(msg):
    f = open('temp/Rap_D.txt', 'w')
    f.write(msg)
    f.close()
