from tkinter import INSERT
import datetime
import dataFunc as daF


def weeklyRap(textfeldweek):
    datei = open("Rap_W.txt", "r")
    for zeile in datei:
        textfeldweek.insert(INSERT, zeile)

def write_titelWrap():
    kw = datetime.date.today().isocalendar()[1]
    name = daF.read_Str('.user_name.txt')
    prename = daF.read_Str('.user_prename.txt')
    data = open('Rap_W.txt', 'w')
    data.write("Wochenrapport: Kw. %d\t" % kw + 'Mitarbeiter: ' + name
               + ' ' + prename + '\n')
    data.close()