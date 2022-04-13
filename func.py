import data


def IP_C():
    instr = -1
    codedit = {'end': -1, 'clock': 0, 'counterclockwise': 1, 'clockwise': 2, 'target': 3}
    raw_code = input()
    if ' ' in raw_code:
        code, instr = raw_code.split(' ')
    else:
        code = raw_code
    return codedit[code], instr


def OP_C():
    pass

def INIT():
    bus_condition = data.BUS_CON
    station_condition = data.STA_CON
    schedule_list = data.SED_LST
