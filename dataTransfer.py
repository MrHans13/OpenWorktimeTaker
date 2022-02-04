def dataWrite(textfile, message):
    data = open(textfile, 'w')
    data.write(message)
    data.close()


def dataRead(textfile):
    data = open(textfile, 'r')
    dataread = data.read()
    data.close()
    return dataread


def read_Time(textfile):
    data = open(textfile, 'r')
    data.read()
    data.close()
    return data


def dataTitel():
    data = open('.datalist.txt', 'w')
    data.write("Datum:\t\tKomission:\tStart:\t\tStop:\t\tStd.\tMin.\tÜberzeit:\n")
    data.close()
