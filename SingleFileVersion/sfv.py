# single file version only for OJ using
# do not edit this file for new features
# ------------------------------------------------
# relocate IO stream
# import sys
# sys.stdin = open('input.txt', mode='r', encoding='utf-8')
# sys.stdout = open('output.txt', mode='w', encoding='utf-8')
# ------------------------------------------------
g_totsta = 0
g_stg = 0
g_dis = 0
g_time = 0
SED_LST = []
tmp_CMD = ()
is_move = 0
NEW_LST = []

class CONFIG:
    TOTAL_STATION = None
    STRATEGY = None
    DISTANCE = None

    def __init__(self, nsta, stg, dis):
        self.TOTAL_STATION = nsta
        self.STRATEGY = stg
        self.DISTANCE = dis


class BUS_CON:
    dric = None  # 0
    station = None  # 0
    move = None  # 0
    dest = None  # '0000000'

    def __init__(self):
        pass

    @classmethod
    def setvar(cls, dric, station, move, dest):
        cls.dric = dric
        cls.station = station
        cls.move = move
        cls.dest = dest


class STA_CON:
    cw_station = None  # '0000000'
    ccw_station = None  # '0000000'

    def __init__(self):
        pass

    @classmethod
    def setvar(cls, cw_station, ccw_station):
        cls.cw_station = cw_station
        cls.ccw_station = ccw_station


# 设定配置参数
def SET_CONFIG():
    # 设置缺省值
    nsta, stg, dis = 5, 'FCFS', 2
    confile = open('dict.dic', mode='r')
    for line in confile:
        if line[0] == '#':
            continue
        tmplist = line.split('=')
        tmplist[0] = tmplist[0].strip()
        tmplist[1] = tmplist[1].strip()
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
    instr = -1  # 默认值，-1代表此code不存在instr
    codediction = {'end': -1, 'clock': 0, 'counterclockwise': 1, 'clockwise': 2, 'target': 3}
    # raw_code = input('->in> ')
    raw_code = input()
    raw_code = raw_code.strip(' ')
    raw_code = raw_code.strip('\t')
    if raw_code == '':
        return -2, instr
    if raw_code[0] == '#':
        return -2, instr
    if ' ' in raw_code:
        code, instr = raw_code.split(' ')
    else:
        code = raw_code
    # 过滤非法指令(code不存在或instr超出最大车站数)
    if code not in codediction or int(instr) > g_totsta:
        print("!--invalid input--!")
        return -2, instr
    return codediction[code], int(instr)


# 控制台输出
def OP_C(bus_condition, sta_condition):
    position = bus_condition.station * g_dis + bus_condition.move
    if position < 0:
        position += g_dis * g_totsta
    print("TIME:%d" % g_time)
    print("BUS:")
    print("position:%d" % position)
    print("target:%s" % bus_condition.dest)
    print("STATION:")
    print("clockwise:%s" % sta_condition.cw_station)
    print("counterclockwise:%s" % sta_condition.ccw_station)


# 结尾控制台输出
def OP_C_E():
    print("end")
    return 0


# 记录总时间
def TIMR():
    global g_time
    g_time += 1


# 计算距离差
def DIS_DIFF(a, b):
    totsta = g_totsta
    dis1 = max(a, b) - min(a, b)
    dis2 = totsta - max(a, b) + min(a, b)
    return min(dis1, dis2)  # 站差


# 判断行车方向
def JUG_DIR(bus_condition=BUS_CON, sed_lst=SED_LST, index=0):
    dis_diff = DIS_DIFF(sed_lst[index][1], bus_condition.station + 1)
    if (sed_lst[index][1] - bus_condition.station - 1) == dis_diff:
        return 1
    elif (sed_lst[index][1] - bus_condition.station - 1) == dis_diff - g_totsta:
        return 1
    else:
        return -1


# 将计划写入计划表
def ADD_SED(code, instr):
    # 计划表为空，插头
    if not SED_LST:
        SED_LST.insert(0, (code, instr))
    elif (code, instr) in SED_LST:
        return 'ST_BY'
    else:
        # ‘FCFS’策略：插尾
        if g_stg == 'FCFS':
            SED_LST.append((code, instr))

        # ‘SSTF’策略或‘SCAN’策略：
        elif g_stg == 'SSTF':
            if (BUS_CON.station+1== instr):
                NEW_LST.append((code, instr))
            # 找出根指令
            i = 0
            while SED_LST[i][0] > 10:
                i += 1
            base_cmd = SED_LST[i]
            basei = i
            # 输入指令是“顺便”指令：
            if DIS_DIFF(BUS_CON.station + 1, instr) < DIS_DIFF(BUS_CON.station + 1, base_cmd[1]) and \
                    DIS_DIFF(instr, base_cmd[1]) < DIS_DIFF(BUS_CON.station + 1, base_cmd[1]):
                if (0 < 2 * (SED_LST[i][1] - BUS_CON.station - 1) <= g_totsta or -2 * g_totsta < 2 * (
                        SED_LST[i][1] - BUS_CON.station - 1) <= -g_totsta):
                    a = 1
                else:
                    a = -1
                # if
                # if (0 < 2*(instr - BUS_CON.station-1) <= g_totsta or -2*g_totsta <2*(instr - BUS_CON.station -1)<= -g_totsta):
                #    b= 1
                # else:
                #    b= -1

                # if (BUS_CON.dric == 1 and code == 2) or (BUS_CON.dric == -1 and code == 1):
                if (code == 1 and a == -1) or (code == 2 and a == 1) or code == 3:
                    code += 10
                    # 判断当前方向
                    dirc = JUG_DIR(index=basei)
                    inspos = 0
                    if inspos >= basei:
                        pass
                    else:
                        if dirc == -1:

                            while (-g_totsta < 2 * (
                                    inspos - SED_LST[inspos + 1][1]) < 0 or
                                   g_totsta < 2 * (inspos - SED_LST[inspos + 1][1]) < 2 * g_totsta) \
                                    and inspos < basei:
                                inspos += 1
                        else:
                            while (-2 * g_totsta < 2 * (
                                    inspos - SED_LST[inspos + 1][1]) < -g_totsta or 0 < 2 * (
                                           inspos - SED_LST[inspos + 1][1]) < g_totsta) and inspos < basei:
                                inspos += 1
                    SED_LST.insert(inspos, (code, instr))
                else:
                    SED_LST.append((code, instr))
            # 输入指令不是“顺便”指令：插尾
            else:
                SED_LST.append((code, instr))
        elif g_stg == 'SCAN':
                if not tmp_CMD:
                    # chawei
                    SED_LST.append((code, instr))
                    tmp_lst = []
                    for i in range(len(SED_LST)):
                        same_dirc = 0
                        totaldis = g_totsta * g_dis
                        if 0 <= (SED_LST[i][1] - (BUS_CON.station + 1)) * g_dis <= totaldis / 2 \
                                or -totaldis <= (
                                SED_LST[i][1] - (BUS_CON.station + 1)) * g_dis <= -totaldis / 2:
                            dric = 1
                        else:
                            dric = -1
                        dis = DIS_DIFF(SED_LST[i][1], BUS_CON.station + 1)
                        if dric == BUS_CON.dric:
                            same_dirc = 1
                        tmp_lst.append((i, dric, dis, same_dirc))
                    tmp_lst.sort(key=lambda x: (x[2], -x[1]))
                    # 找出最短时间指令索引
                    if not tmp_lst:
                        return
                    else:
                        short_index = tmp_lst[0][0]
                        # 将最短时间指令插入计划表首位
                        SED_LST.insert(0, SED_LST[short_index])
                        SED_LST.pop(short_index + 1)
                else:

                    # 找出根指令
                    i = 0
                    while SED_LST[i][0] > 10:
                        i += 1
                    base_cmd = SED_LST[i]
                    basei = i
                    # 输入指令是“顺便”指令：
                    if DIS_DIFF(BUS_CON.station + 1, instr) < DIS_DIFF(BUS_CON.station + 1, base_cmd[1]) and \
                            DIS_DIFF(instr, base_cmd[1]) < DIS_DIFF(BUS_CON.station + 1, base_cmd[1]):
                        code += 10
                        # 判断当前方向
                        dirc = JUG_DIR(index=basei)
                        inspos = 0
                        if inspos >= basei:
                            pass
                        else:
                            if dirc == -1:

                                while (-g_totsta < 2 * (
                                        inspos - SED_LST[inspos + 1][1]) < 0 or
                                       g_totsta < 2 * (
                                               inspos - SED_LST[inspos + 1][1]) < 2 * g_totsta) \
                                        and inspos < basei:
                                    inspos += 1
                            else:
                                while (-2 * g_totsta < 2 * (
                                        inspos - SED_LST[inspos + 1][1]) < -g_totsta or 0 < 2 * (
                                               inspos - SED_LST[inspos + 1][
                                           1]) < g_totsta) and inspos < basei:
                                    inspos += 1
                        SED_LST.insert(inspos, (code, instr))
                    else:
                        SED_LST.append((code, instr))
            # 输入指令不是“顺便”指令：插尾
        else:
            SED_LST.append((code, instr))


# 将计划表内的计划写入状态数据类
def ADD_CON():
    for i in range(len(SED_LST)):
        # 写入STA_CON.ccw_station
        if SED_LST[i][0] % 10 == 1:
            temp_list = list(STA_CON.ccw_station)
            temp_list[SED_LST[i][1] - 1] = '1'
            STA_CON.ccw_station = ''.join(temp_list)
        # 写入STA_CON.cw_station
        elif SED_LST[i][0] % 10 == 2:
            temp_list = list(STA_CON.cw_station)
            temp_list[SED_LST[i][1] - 1] = '1'
            STA_CON.cw_station = ''.join(temp_list)
        # 写入BUS_CON.dest
        elif SED_LST[i][0] % 10 == 3:
            temp_list = list(BUS_CON.dest)
            temp_list[SED_LST[i][1] - 1] = '1'
            BUS_CON.dest = ''.join(temp_list)


# 删除已完成计划（默认清除首条命令）
def REMOVE_SED(index=0):
    # default
    SED_LST.pop(index)


# SSTF策略，根指令，删除该站全部计划后需要重新排序SED_LST
def REMOVE_SED_SSTF(del_sta):
    if (1, del_sta) in SED_LST:
        SED_LST.remove((1, del_sta))
    if (2, del_sta) in SED_LST:
        SED_LST.remove((2, del_sta))
    if (3, del_sta) in SED_LST:
        SED_LST.remove((3, del_sta))
    tmp_lst = []
    for i in range(len(SED_LST)):
        totaldis = g_totsta * g_dis
        if 0 <= (SED_LST[i][1] - (BUS_CON.station + 1)) * g_dis <= totaldis / 2 \
                or -totaldis <= (SED_LST[i][1] - (BUS_CON.station + 1)) * g_dis <= -totaldis / 2:
            dric = 1
        else:
            dric = -1
        dis = DIS_DIFF(SED_LST[i][1], BUS_CON.station + 1)

        tmp_lst.append((i, dric, dis))

    tmp_lst.sort(key=lambda x: (x[2], -x[1]))
    # 找出最短时间指令索引
    if not tmp_lst:
        return
    else:
        short_index = tmp_lst[0][0]
        # 将最短时间指令插入计划表首位
        SED_LST.insert(0, SED_LST[short_index])
        SED_LST.pop(short_index + 1)


# SCAN策略，根指令，删除该计划后需要重新排序SED_LST
def REMOVE_SED_SCAN():
    SED_LST.pop(0)
    tmp_lst = []
    for i in range(len(SED_LST)):
        same_dirc = 0
        totaldis = g_totsta * g_dis
        if 0 <= (SED_LST[i][1] - (BUS_CON.station + 1)) * g_dis <= totaldis / 2 \
                or -totaldis <= (SED_LST[i][1] - (BUS_CON.station + 1)) * g_dis <= -totaldis / 2:
            dric = 1
        else:
            dric = -1
        dis = DIS_DIFF(SED_LST[i][1], BUS_CON.station + 1)
        if dric == BUS_CON.dric:
            same_dirc = 1
        tmp_lst.append((i, dric, dis, same_dirc))
    tmp_lst.sort(key=lambda x: (-x[3], x[2]))
    # 找出最短时间指令索引
    if not tmp_lst:
        return
    else:
        short_index = tmp_lst[0][0]
        # 将最短时间指令插入计划表首位
        SED_LST.insert(0, SED_LST[short_index])
        SED_LST.pop(short_index + 1)


# 公交车行车
def BUS_DRIVE():
    # 根据方向修改move状态
    BUS_CON.move += BUS_CON.dric
    # move、station进位操作
    if BUS_CON.move == g_dis:
        BUS_CON.move = 0
        BUS_CON.station += 1
    elif BUS_CON.move == -g_dis:
        BUS_CON.move = 0
        BUS_CON.station -= 1
    # station负值修正
    if BUS_CON.station < 0:
        BUS_CON.station += g_totsta
    # station超出范围修正
    if BUS_CON.station >= g_totsta:
        BUS_CON.station -= g_totsta


def first_sort_cert(tup):
    return DIS_DIFF(1, tup[1])


def BUS_MOV():
    global is_move, tmp_CMD
    # 判断计划表是否为空，如为空返回'ST_BY'状态
    if not SED_LST:
        return 'ST_BY'

    else:
        is_move += 1
        if is_move == 1 and (g_stg == 'SCAN' or g_stg == 'SSTF'):
            SED_LST.sort(key=first_sort_cert)

        # 执行新计划时判断车辆方向（比较当前计划与存储计划是否相同，tmpCMD初值为空，两计划不同时即为新计划）
        if SED_LST[0] != tmp_CMD:
            BUS_CON.dric = JUG_DIR()

        # 将当前计划复制到存储计划
        tmp_CMD = SED_LST[0]
        # 将当前计划目的车站复制到存储目的车站
        cur_tar_station = SED_LST[0][1]
        while True:
            # 是否到站
            if BUS_CON.station == SED_LST[0][1] - 1 and BUS_CON.move == 0:
                # 如策略为SSTF，根指令
                if g_stg == 'SSTF' and SED_LST[0][0] < 10:
                    DEL_CON_SSTF(SED_LST[0][1])
                # 如策略为SCAN，根指令
                elif g_stg == 'SCAN' and SED_LST[0][0] < 10:
                    DEL_CON_SCAN()
                else:
                    # 到站，执行上、下车指令
                    if SED_LST[0][0] % 10 == 1 or SED_LST[0][0] % 10 == 2:
                        PSG_U(SED_LST[0][0], BUS_CON.station)
                    elif SED_LST[0][0] % 10 == 3:
                        PSG_D(BUS_CON.station)

                # 如命令表已空，返回'ST_BY'状态
                if not SED_LST:
                    return 'ST_BY'
                # 如下一条指令位于同站（当前计划目的车站与存储目的车站相同），继续执行上下车指令
                if SED_LST[0][1] != cur_tar_station:
                    break
            else:
                # 没到站，执行行车指令
                BUS_DRIVE()
                break


# SSTF策略，根指令，同时清除三种状态
def DEL_CON_SSTF(num):
    # 清除计划
    REMOVE_SED_SSTF(num)
    # 清除ccw站台状态
    templststr = list(STA_CON.ccw_station)
    templststr[num - 1] = '0'
    STA_CON.ccw_station = ''.join(templststr)
    # 清除cw站台状态
    templststr = list(STA_CON.cw_station)
    templststr[num - 1] = '0'
    STA_CON.cw_station = ''.join(templststr)
    # 清除车辆target状态
    templststr = list(BUS_CON.dest)
    templststr[num - 1] = '0'
    BUS_CON.dest = ''.join(templststr)
    # 加入新表状态
    if NEW_LST:
        if NEW_LST[0][0] == 1:
            templststr = list(STA_CON.ccw_station)
            templststr[num - 1] = '1'
            STA_CON.ccw_station = ''.join(templststr)
        elif NEW_LST[0][0] == 2:
            templststr = list(STA_CON.cw_station)
            templststr[num - 1] = '1'
            STA_CON.cw_station = ''.join(templststr)
        elif NEW_LST[0][0] == 3:
            templststr = list(BUS_CON.dest)
            templststr[num - 1] = '1'
            BUS_CON.dest = ''.join(templststr)


# SCAN策略，根指令
def DEL_CON_SCAN():
    num = BUS_CON.station + 1
    # 清除ccw站台状态
    if SED_LST[0][0] % 10 == 1:
        templststr = list(STA_CON.ccw_station)
        templststr[num - 1] = '0'
        STA_CON.ccw_station = ''.join(templststr)
    # 清除cw站台状态
    elif SED_LST[0][0] % 10 == 2:
        templststr = list(STA_CON.cw_station)
        templststr[num - 1] = '0'
        STA_CON.cw_station = ''.join(templststr)
    # 清除车辆target状态
    elif SED_LST[0][0] % 10 == 3:
        templststr = list(BUS_CON.dest)
        templststr[num - 1] = '0'
        BUS_CON.dest = ''.join(templststr)
    # 清除计划
    REMOVE_SED_SCAN()


# 乘客上车（包括cw、ccw指令）-num为车辆所在车站号
def PSG_U(code, num):
    # 清除计划（已完成）
    REMOVE_SED()
    # 清除ccw站台状态
    if code % 10 == 1:
        templststr = list(STA_CON.ccw_station)
        templststr[num] = '0'
        STA_CON.ccw_station = ''.join(templststr)
    # 清除cw站台状态
    elif code % 10 == 2:
        templststr = list(STA_CON.cw_station)
        templststr[num] = '0'
        STA_CON.cw_station = ''.join(templststr)


# 乘客下车（target指令）-num为车辆所在车站号
def PSG_D(num):
    # 清除计划（已完成）
    REMOVE_SED()
    # 清除车辆target状态
    templststr = list(BUS_CON.dest)
    templststr[num] = '0'
    BUS_CON.dest = ''.join(templststr)


if __name__ == '__main__':

    # 输入配置参数并配置
    g_totsta, g_stg, g_dis = SET_CONFIG()
    CONFIG(nsta=g_totsta, stg=g_stg, dis=g_dis)

    # 初始化py中的变量
    BUS_CON.setvar(0, 0, 0, '0' * g_totsta)
    STA_CON.setvar('0' * g_totsta, '0' * g_totsta)

    # 运行
    OP_C(BUS_CON, STA_CON)  # 第一次运行，输出结果
    while True:
        code, instr = IP_C()
        if code == -2:
            continue
        if code == -1:
            OP_C_E()
            exit(0)
        elif code == 1 or code == 2 or code == 3:
            # 执行ADD_SED函数
            state = ADD_SED(code, instr)
            if state == 'ST_BY':
                pass
            # 执行ADD_CON函数
            ADD_CON()
            # print("<-sedlst->\n", SED_LST)
        elif code == 0:
            # 执行BUS_MOV函数
            if BUS_MOV() == 'ST_BY':
                pass
            if NEW_LST:
                SED_LST.append(NEW_LST[0])
                NEW_LST.pop(0)
            # 执行TIMR函数
            TIMR()
            # 执行OP_C函数
            OP_C(BUS_CON, STA_CON)
