import data
import gl_VAR
import os


# 设定配置参数
# 设定配置参数
def SET_CONFIG():
    # 设置缺省值
    nsta, stg, dis = 5, 'FCFS', 2
    confile = open('dict.dic', mode='r')
    for line in confile:
        if line[0] == '#':
            continue
        tmplist = line.split('=')
        tmplist[0] = tmplist[0].strip(' ')
        tmplist[1] = tmplist[1].strip(' ')
        tmplist[1] = tmplist[1].strip('\n')

        if tmplist[0] == 'TOTAL_STATION':
            nsta = int(tmplist[1])
        elif tmplist[0] == 'STRATEGY':
            stg = tmplist[1]
            #stg = stg.strip('\n')
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
    if code not in codediction or int(instr) > gl_VAR.g_totsta:
        print("!--invalid input--!")
        return -2, instr
    return codediction[code], int(instr)


# 控制台输出
def OP_C(bus_condition, sta_condition):
    position = bus_condition.station * gl_VAR.g_dis + bus_condition.move
    if position < 0:
        position += gl_VAR.g_dis * gl_VAR.g_totsta
    print("TIME:%d" % gl_VAR.g_time)
    print("BUS:")
    print("position:%d" % position)
    print("target:%s" % bus_condition.dest)
    print("STATION:")
    print("clockwise:%s" % sta_condition.cw_station)
    print("counterclockwise:%s" % sta_condition.ccw_station)
    # print("position",%s bus_condition)
    # print(position),
    # print()


# 结尾控制台输出
def OP_C_E():
    print("end")
    return 0


# 文件输出（动画）
def OP_C_F(bus_condition):
    position = bus_condition.station * gl_VAR.g_dis + bus_condition.move
    if position < 0:
        position += gl_VAR.g_dis * gl_VAR.g_totsta

    # write to file
    f = open('GUI/outfile.txt', 'a')
    f.write("TIME:%d\n" % gl_VAR.g_time)
    f.write("position:%d\n" % position)
    if data.SED_LST:
        f.write("target:%s\n" % str(data.SED_LST[0]))
    else:
        f.write("target:-1\n")
    f.close()


# 记录总时间
def TIMR():
    gl_VAR.g_time += 1


# 计算距离差
def DIS_DIFF(a, b):
    totsta = gl_VAR.g_totsta
    dis1 = max(a, b) - min(a, b)
    dis2 = totsta - max(a, b) + min(a, b)
    return min(dis1, dis2)  # 站差


# 判断行车方向
def JUG_DIR(bus_condition=data.BUS_CON, sed_lst=data.SED_LST, index=0):
    dis_diff = DIS_DIFF(sed_lst[index][1], bus_condition.station + 1)
    if (sed_lst[index][1] - bus_condition.station - 1) == dis_diff:
        return 1
    elif (sed_lst[index][1] - bus_condition.station - 1) == dis_diff - gl_VAR.g_totsta:
        return 1
    else:
        return -1


# 将计划写入计划表
def ADD_SED(code, instr):
    # 计划表为空，插头
    if not data.SED_LST:
        data.SED_LST.insert(0, (code, instr))
    elif (code, instr) in data.SED_LST:
        return 'ST_BY'
    else:
        # ‘FCFS’策略：插尾
        if gl_VAR.g_stg == 'FCFS':
            data.SED_LST.append((code, instr))

        # ‘SSTF’策略或‘SCAN’策略：
        elif gl_VAR.g_stg == 'SSTF':
            if (data.BUS_CON.station+1== instr):
                data.NEW_LST.append((code, instr))
            else:
                # 找出根指令
                i = 0
                while data.SED_LST[i][0] > 10:
                    i += 1
                base_cmd = data.SED_LST[i]
                basei = i
                # 输入指令是“顺便”指令：
                if DIS_DIFF(data.BUS_CON.station + 1, instr) < DIS_DIFF(data.BUS_CON.station + 1, base_cmd[1]) and \
                        DIS_DIFF(instr, base_cmd[1]) < DIS_DIFF(data.BUS_CON.station + 1, base_cmd[1]):
                    if (0 < 2 * (data.SED_LST[i][
                                     1] - data.BUS_CON.station - 1) <= gl_VAR.g_totsta or -2 * gl_VAR.g_totsta < 2 * (
                            data.SED_LST[i][1] - data.BUS_CON.station - 1) <= -gl_VAR.g_totsta):
                        a = 1
                    else:
                        a = -1
                    # if
                    # if (0 < 2*(instr - data.BUS_CON.station-1) <= gl_VAR.g_totsta or -2*gl_VAR.g_totsta <2*(instr - data.BUS_CON.station -1)<= -gl_VAR.g_totsta):
                    #    b= 1
                    # else:
                    #    b= -1

                    # if (data.BUS_CON.dric == 1 and code == 2) or (data.BUS_CON.dric == -1 and code == 1):
                    if (code == 1 and a == -1) or (code == 2 and a == 1) or code == 3:
                        code += 10
                        # 判断当前方向
                        dirc = JUG_DIR(index=basei)
                        inspos = 0
                        if inspos >= basei:
                            pass
                        else:
                            if dirc == -1:

                                while (-gl_VAR.g_totsta < 2 * (
                                        inspos - data.SED_LST[inspos + 1][1]) < 0 or
                                       gl_VAR.g_totsta < 2 * (inspos - data.SED_LST[inspos + 1][1]) < 2 * gl_VAR.g_totsta) \
                                        and inspos < basei:
                                    inspos += 1
                            else:
                                while (-2 * gl_VAR.g_totsta < 2 * (
                                        inspos - data.SED_LST[inspos + 1][1]) < -gl_VAR.g_totsta or 0 < 2 * (
                                               inspos - data.SED_LST[inspos + 1][1]) < gl_VAR.g_totsta) and inspos < basei:
                                    inspos += 1
                        data.SED_LST.insert(inspos, (code, instr))
                    else:
                        data.SED_LST.append((code, instr))
                # 输入指令不是“顺便”指令：插尾
                else:
                    data.SED_LST.append((code, instr))
        elif gl_VAR.g_stg == 'SCAN':
            if (data.BUS_CON.station+1== instr):
                data.NEW_LST.append((code, instr))
            if not data.tmp_CMD:
                # chawei
                data.SED_LST.append((code, instr))
                tmp_lst = []
                for i in range(len(data.SED_LST)):
                    same_dirc = 0
                    totaldis = gl_VAR.g_totsta * gl_VAR.g_dis
                    if 0 <= (data.SED_LST[i][1] - (data.BUS_CON.station + 1)) * gl_VAR.g_dis <= totaldis / 2 \
                            or -totaldis <= (
                            data.SED_LST[i][1] - (data.BUS_CON.station + 1)) * gl_VAR.g_dis <= -totaldis / 2:
                        dric = 1
                    else:
                        dric = -1
                    dis = DIS_DIFF(data.SED_LST[i][1], data.BUS_CON.station + 1)
                    if dric == data.BUS_CON.dric:
                        same_dirc = 1
                    tmp_lst.append((i, dric, dis, same_dirc))
                tmp_lst.sort(key=lambda x: (x[2],-x[1]))
                # 找出最短时间指令索引
                if not tmp_lst:
                    return
                else:
                    short_index = tmp_lst[0][0]
                    # 将最短时间指令插入计划表首位
                    data.SED_LST.insert(0, data.SED_LST[short_index])
                    data.SED_LST.pop(short_index + 1)
            else:

                # 找出根指令
                i = 0
                while data.SED_LST[i][0] > 10:
                    i += 1
                base_cmd = data.SED_LST[i]
                basei = i
                # 输入指令是“顺便”指令：
                if DIS_DIFF(data.BUS_CON.station + 1, instr) < DIS_DIFF(data.BUS_CON.station + 1, base_cmd[1]) and \
                        DIS_DIFF(instr, base_cmd[1]) < DIS_DIFF(data.BUS_CON.station + 1, base_cmd[1]):
                    code += 10
                    # 判断当前方向
                    dirc = JUG_DIR(index=basei)
                    inspos = 0
                    if inspos >= basei:
                        pass
                    else:
                        if dirc == -1:

                            while (-gl_VAR.g_totsta < 2 * (
                                    inspos - data.SED_LST[inspos + 1][1]) < 0 or
                                   gl_VAR.g_totsta < 2 * (inspos - data.SED_LST[inspos + 1][1]) < 2 * gl_VAR.g_totsta) \
                                    and inspos < basei:
                                inspos += 1
                        else:
                            while (-2 * gl_VAR.g_totsta < 2 * (
                                    inspos - data.SED_LST[inspos + 1][1]) < -gl_VAR.g_totsta or 0 < 2 * (
                                           inspos - data.SED_LST[inspos + 1][1]) < gl_VAR.g_totsta) and inspos < basei:
                                inspos += 1
                    data.SED_LST.insert(inspos, (code, instr))
                else:
                    data.SED_LST.append((code, instr))
            # 输入指令不是“顺便”指令：插尾
        else:
            data.SED_LST.append((code, instr))


# 将计划表内的计划写入状态数据类
def ADD_CON():
    for i in range(len(data.SED_LST)):
        # 写入STA_CON.ccw_station
        if data.SED_LST[i][0] % 10 == 1:
            temp_list = list(data.STA_CON.ccw_station)
            temp_list[data.SED_LST[i][1] - 1] = '1'
            data.STA_CON.ccw_station = ''.join(temp_list)
        # 写入STA_CON.cw_station
        elif data.SED_LST[i][0] % 10 == 2:
            temp_list = list(data.STA_CON.cw_station)
            temp_list[data.SED_LST[i][1] - 1] = '1'
            data.STA_CON.cw_station = ''.join(temp_list)
        # 写入BUS_CON.dest
        elif data.SED_LST[i][0] % 10 == 3:
            temp_list = list(data.BUS_CON.dest)
            temp_list[data.SED_LST[i][1] - 1] = '1'
            data.BUS_CON.dest = ''.join(temp_list)


# 删除已完成计划（默认清除首条命令）
def REMOVE_SED(index=0):
    # default
    data.SED_LST.pop(index)


# SSTF策略，根指令，删除该站全部计划后需要重新排序SED_LST
def REMOVE_SED_SSTF(del_sta):
    if (1, del_sta) in data.SED_LST:
        data.SED_LST.remove((1, del_sta))
    if (2, del_sta) in data.SED_LST:
        data.SED_LST.remove((2, del_sta))
    if (3, del_sta) in data.SED_LST:
        data.SED_LST.remove((3, del_sta))

    tmp_lst = []
    for i in range(len(data.SED_LST)):
        totaldis = gl_VAR.g_totsta * gl_VAR.g_dis
        if 0 <= (data.SED_LST[i][1] - (data.BUS_CON.station + 1)) * gl_VAR.g_dis <= totaldis / 2 \
                or -totaldis <= (data.SED_LST[i][1] - (data.BUS_CON.station + 1)) * gl_VAR.g_dis <= -totaldis / 2:
            dric = 1
        else:
            dric = -1
        dis = DIS_DIFF(data.SED_LST[i][1], data.BUS_CON.station + 1)

        tmp_lst.append((i, dric, dis))

    tmp_lst.sort(key=lambda x: (x[2], -x[1]))
    # 找出最短时间指令索引
    if not tmp_lst:
        return
    else:
        short_index = tmp_lst[0][0]
        # 将最短时间指令插入计划表首位
        data.SED_LST.insert(0, data.SED_LST[short_index])
        data.SED_LST.pop(short_index + 1)


# SCAN策略，根指令，删除该计划后需要重新排序SED_LST
def REMOVE_SED_SCAN():
    data.SED_LST.pop(0)
    tmp_lst = []
    for i in range(len(data.SED_LST)):
        same_dirc = 0
        totaldis = gl_VAR.g_totsta * gl_VAR.g_dis
        if 0 <= (data.SED_LST[i][1] - (data.BUS_CON.station + 1)) * gl_VAR.g_dis <= totaldis / 2 \
                or -totaldis <= (data.SED_LST[i][1] - (data.BUS_CON.station + 1)) * gl_VAR.g_dis <= -totaldis / 2:
            dric = 1
        else:
            dric = -1
        dis = DIS_DIFF(data.SED_LST[i][1], data.BUS_CON.station + 1)
        if dric == data.BUS_CON.dric:
            same_dirc = 1
        tmp_lst.append((i, dric, dis, same_dirc))
    tmp_lst.sort(key=lambda x: (-x[3], x[2]))
    # 找出最短时间指令索引
    if not tmp_lst:
        return
    else:
        short_index = tmp_lst[0][0]
        # 将最短时间指令插入计划表首位
        data.SED_LST.insert(0, data.SED_LST[short_index])
        data.SED_LST.pop(short_index + 1)


# 公交车行车
def BUS_DRIVE():
    # 根据方向修改move状态
    data.BUS_CON.move += data.BUS_CON.dric
    # move、station进位操作
    if data.BUS_CON.move == gl_VAR.g_dis:
        data.BUS_CON.move = 0
        data.BUS_CON.station += 1
    elif data.BUS_CON.move == -gl_VAR.g_dis:
        data.BUS_CON.move = 0
        data.BUS_CON.station -= 1
    # station负值修正
    if data.BUS_CON.station < 0:
        data.BUS_CON.station += gl_VAR.g_totsta
    # station超出范围修正
    if data.BUS_CON.station >= gl_VAR.g_totsta:
        data.BUS_CON.station -= gl_VAR.g_totsta


def first_sort_cert(tup):
    return DIS_DIFF(1, tup[1])


def BUS_MOV():
    # 判断计划表是否为空，如为空返回'ST_BY'状态
    if not data.SED_LST:
        return 'ST_BY'

    else:
        data.is_move += 1
        if data.is_move == 1 and (gl_VAR.g_stg == 'SCAN' or gl_VAR.g_stg == 'SSTF'):
            data.SED_LST.sort(key=first_sort_cert)

        # 执行新计划时判断车辆方向（比较当前计划与存储计划是否相同，tmpCMD初值为空，两计划不同时即为新计划）
        if data.SED_LST[0] != data.tmp_CMD:
            data.BUS_CON.dric = JUG_DIR()

        # 将当前计划复制到存储计划
        data.tmp_CMD = data.SED_LST[0]
        # 将当前计划目的车站复制到存储目的车站
        cur_tar_station = data.SED_LST[0][1]
        while True:
            # 是否到站
            if data.BUS_CON.station == data.SED_LST[0][1] - 1 and data.BUS_CON.move == 0:
                # 如策略为SSTF，根指令
                if gl_VAR.g_stg == 'SSTF' and data.SED_LST[0][0] < 10:
                    DEL_CON_SSTF(data.SED_LST[0][1])
                # 如策略为SCAN，根指令
                elif gl_VAR.g_stg == 'SCAN' and data.SED_LST[0][0] < 10:
                    DEL_CON_SCAN()
                else:
                    # 到站，执行上、下车指令
                    if data.SED_LST[0][0] % 10 == 1 or data.SED_LST[0][0] % 10 == 2:
                        PSG_U(data.SED_LST[0][0], data.BUS_CON.station)
                    elif data.SED_LST[0][0] % 10 == 3:
                        PSG_D(data.BUS_CON.station)

                # 如命令表已空，返回'ST_BY'状态
                if not data.SED_LST:
                    return 'ST_BY'
                # 如下一条指令位于同站（当前计划目的车站与存储目的车站相同），继续执行上下车指令
                if data.SED_LST[0][1] != cur_tar_station:
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
    templststr = list(data.STA_CON.ccw_station)
    templststr[num - 1] = '0'
    data.STA_CON.ccw_station = ''.join(templststr)
    # 清除cw站台状态
    templststr = list(data.STA_CON.cw_station)
    templststr[num - 1] = '0'
    data.STA_CON.cw_station = ''.join(templststr)
    # 清除车辆target状态
    templststr = list(data.BUS_CON.dest)
    templststr[num - 1] = '0'
    data.BUS_CON.dest = ''.join(templststr)
    # 加入新表状态
    if data.NEW_LST:
        if data.NEW_LST[0][0] == 1:
            templststr = list(data.STA_CON.ccw_station)
            templststr[num - 1] = '1'
            data.STA_CON.ccw_station = ''.join(templststr)
        elif data.NEW_LST[0][0] == 2:
            templststr = list(data.STA_CON.cw_station)
            templststr[num - 1] = '1'
            data.STA_CON.cw_station = ''.join(templststr)
        elif data.NEW_LST[0][0] == 3:
            templststr = list(data.BUS_CON.dest)
            templststr[num - 1] = '1'
            data.BUS_CON.dest = ''.join(templststr)


# SCAN策略，根指令
def DEL_CON_SCAN():
    num = data.BUS_CON.station + 1
    # 清除ccw站台状态
    if data.SED_LST[0][0] % 10 == 1:
        templststr = list(data.STA_CON.ccw_station)
        templststr[num - 1] = '0'
        data.STA_CON.ccw_station = ''.join(templststr)
    # 清除cw站台状态
    elif data.SED_LST[0][0] % 10 == 2:
        templststr = list(data.STA_CON.cw_station)
        templststr[num - 1] = '0'
        data.STA_CON.cw_station = ''.join(templststr)
    # 清除车辆target状态
    elif data.SED_LST[0][0] % 10 == 3:
        templststr = list(data.BUS_CON.dest)
        templststr[num - 1] = '0'
        data.BUS_CON.dest = ''.join(templststr)
    # 清除计划
    REMOVE_SED_SCAN()
    if data.NEW_LST:
        if data.NEW_LST[0][0] == 1:
            templststr = list(data.STA_CON.ccw_station)
            templststr[num - 1] = '1'
            data.STA_CON.ccw_station = ''.join(templststr)
        elif data.NEW_LST[0][0] == 2:
            templststr = list(data.STA_CON.cw_station)
            templststr[num - 1] = '1'
            data.STA_CON.cw_station = ''.join(templststr)
        elif data.NEW_LST[0][0] == 3:
            templststr = list(data.BUS_CON.dest)
            templststr[num - 1] = '1'
            data.BUS_CON.dest = ''.join(templststr)

# 乘客上车（包括cw、ccw指令）-num为车辆所在车站号
def PSG_U(code, num):
    # 清除计划（已完成）
    REMOVE_SED()
    # 清除ccw站台状态
    if code % 10 == 1:
        templststr = list(data.STA_CON.ccw_station)
        templststr[num] = '0'
        data.STA_CON.ccw_station = ''.join(templststr)
    # 清除cw站台状态
    elif code % 10 == 2:
        templststr = list(data.STA_CON.cw_station)
        templststr[num] = '0'
        data.STA_CON.cw_station = ''.join(templststr)


# 乘客下车（target指令）-num为车辆所在车站号
def PSG_D(num):
    # 清除计划（已完成）
    REMOVE_SED()
    # 清除车辆target状态
    templststr = list(data.BUS_CON.dest)
    templststr[num] = '0'
    data.BUS_CON.dest = ''.join(templststr)
