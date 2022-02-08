def write_Stat_Data(textfile, msg):
    f = open(textfile, 'w')
    f.write(msg)
    f.close()


def read_Str(textfile):
    f = open(textfile, 'r')
    data = f.read()
    f.close()
    return data


def read_Int(textfile):
    f = open(textfile, 'r')
    data = int(f.read())
    f.close()
    return data


def write_titelWrap():
    data = open('WeeklyRapport.txt', 'w')
    data.write("Datum:\t\tKomission:\tStart:\tStop:\tZeit:\tÜ-Zeit:\n")
    data.close()


def write_titelDrap():
    data = open('DailyRapport.txt', 'w')
    data.write("Datum:\t\tKomission:\t\tStart:\tStop:\tZeit:\tÜ-Zeit:\n")
    data.close()


def data_clear(textfile):
    f = open(textfile, 'w')
    f.write('')
    f.close()


def state_Reset(textfile):
    f = open(textfile, 'w')
    f.write('0')
    f.close()
