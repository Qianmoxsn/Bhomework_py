import data
import gl_VAR


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


# 控制台输入
def IP_C():
    instr = -1
    codediction = {'end': -1, 'clock': 0, 'counterclockwise': 1, 'clockwise': 2, 'target': 3}
    raw_code = input('->in> ')
    if ' ' in raw_code:
        code, instr = raw_code.split(' ')
    else:
        code = raw_code

    if code not in codediction:
        print("!--invalid input--!")
        return -2, instr
    return codediction[code], instr


# 控制台输出
def OP_C(bus_condition, sta_condition):
    position = bus_condition.station * gl_VAR.g_dis + bus_condition.move
    print("BUS:")
    print("position:%d" % position)
    print("target: %s" % bus_condition.dest)
    print("STATION:")
    print("clockwise: %s" % sta_condition.cw_station)
    print("counterclockwise: %s" % sta_condition.ccw_station)


# 结尾控制台输出
def OP_C_E(sta_condition):
    print("end\nSTATION:")
    print("clockwise: %s" % sta_condition.cw_station)
    print("counterclockwise: %s" % sta_condition.ccw_station)
    return 0


# 记录总时间
def TIMR():
    gl_VAR.g_time += 1


class BUS_ACT:
    def STG(self):
        pass

    def BUS_MOV(self):
        pass

    def PSG_U(self):
        pass

    def PSG_D(self):
        pass
