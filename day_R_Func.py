from tkinter import INSERT
import dataFunc as daF


def dailyRap(textfeldday):
    datei = open("DailyRapport.txt", "r")
    textfeldday.delete("1.0", "end")
    for zeile in datei:
        textfeldday.insert(INSERT, zeile)


def write_titelDrap():
    daF.write_Stat_Data('DailyRapport.txt', "Datum:\t\tKomission:\t\tStart:\tStop:\tZeit:\tÜ-Zeit:\n")
    daF.write_Stat_Data('.state_file.txt', '1')
    daF.write_Stat_Data('.state_prog.txt', '2')
