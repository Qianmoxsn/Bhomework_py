import funcs
import data
import gl_VAR
if __name__ == '__main__':

    # 输入配置参数并配置
    gl_VAR.g_totsta, gl_VAR.g_stg, gl_VAR.g_dis = funcs.SET_CONFIG()
    data.CONFIG(nsta=gl_VAR.g_totsta, stg=gl_VAR.g_stg, dis=gl_VAR.g_dis)

    # 初始化data.py中的变量
    data.BUS_CON.setvar(0, 0, 0, '0' * gl_VAR.g_totsta)
    data.STA_CON.setvar('0' * gl_VAR.g_totsta, '0' * gl_VAR.g_totsta)

    # 运行
    funcs.OP_C(data.BUS_CON, data.STA_CON)  # 第一次运行，输出结果
    while True:
        code, instr = funcs.IP_C()
        if code == -2:
            continue
        if code == -1:
            funcs.OP_C_E()
            exit(-1)
        elif code == 1 or code == 2 or code == 3:
            # 执行ADD_SED函数
            state = funcs.ADD_SED(code, instr)
            if state == 'ST_BY':
                pass
            # 执行ADD_CON函数
            funcs.ADD_CON()
            # print("<-sedlst->\n", data.SED_LST)
        elif code == 0:
            # 执行BUS_MOV函数
            if funcs.BUS_MOV() == 'ST_BY':
                pass
            # 执行TIMR函数
            funcs.TIMR()
            # 执行OP_C函数
            funcs.OP_C(data.BUS_CON, data.STA_CON)
