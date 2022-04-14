import data


def SET_CONFIG():
    # 设置缺省值
    nsta, stg, dis = 5, 'FCFS', 2
    confile = open('dict.dic', mode='r')
    for line in confile:
        if line[0] == '#':
            continue
        tmplist = line.split(' = ')
        if tmplist[0] == 'TOTAL_STATION':
            nsta = int(tmplist[1])
        elif tmplist[0] == 'STRATEGY':
            stg = tmplist[1]
            stg = stg.strip('\n')
        elif tmplist[0] == 'DISTANCE':
            dis = int(tmplist[1])
    confile.close()

    return nsta, stg, dis


def IP_C():
    instr = -1
    codediction = {'end': -1, 'clock': 0, 'counterclockwise': 1, 'clockwise': 2, 'target': 3}
    raw_code = input()
    if ' ' in raw_code:
        code, instr = raw_code.split(' ')
    else:
        code = raw_code
    return codediction[code], instr


def OP_C():
    pass


def OP_C_E():
    pass

def INIT():
    pass


def TIMR():
    pass


class BUS_ACT:
    def STG(self):
        pass

    def BUS_MOV(self):
        pass

    def PSG_U(self):
        pass

    def PSG_D(self):
        pass
