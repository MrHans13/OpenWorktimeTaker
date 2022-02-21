from tkinter import INSERT
import Func_Data as daF


def weeklyRap(textfeldweek):
    datei = open("temp/Rap_W.txt", "r")
    textfeldweek.delete("1.0", "end")
    for zeile in datei:
        textfeldweek.insert(INSERT, zeile)


def write_titelWrap():
    lname = daF.get_str_Data('temp/user_hpf.txt', 'u_name')
    pname = daF.get_str_Data('temp/user_hpf.txt', 'u_prename')
    kw = daF.get_str_Data('temp/.act_date.txt', 'kw')
    data = open('temp/Rap_W.txt', 'w')
    data.write("Wochenrapport: \tKw: " + kw +
               '\tMitarbeiter: ' + lname
               + ' ' + pname + '\n')
    data.close()

def a_data_wRap(msg):
    f = open('temp/Rap_W.txt', 'a')
    f.write(msg)
    f.close()