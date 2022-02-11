
def write_Stat_Data(textfile, msg):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'w')
    f.write(str(msg))
    f.close()


def append_Data(textfile, msg):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'a')
    f.write(msg)
    f.close()


def read_List(list_file):
    comm_list_file = open('/home/peti/Projects/OpenWtTaker/temp/' + list_file, 'r')
    comm_list = comm_list_file.read().split()
    comm_list_file.close()
    return comm_list


def r_Str_temp(textfile):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'r')
    data = f.read()
    f.close()
    return data

def read_Str(textfile):
    f = open(textfile, 'r')
    data = f.read()
    f.close()
    return data

def read_Int(textfile):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'r')
    data = int(f.read())
    f.close()
    return data

def r_Int_temp(textfile):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'r')
    data = int(f.read())
    f.close()
    return data




def data_clear(textfile):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'w')
    f.write('')
    f.close()


def state_Reset(textfile):
    f = open('/home/peti/Projects/OpenWtTaker/temp/' + textfile, 'w')
    f.write('0')
    f.close()
