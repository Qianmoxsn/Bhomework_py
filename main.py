import funcs
import data
import gl_VAR
if __name__ == '__main__':

    # 输入配置参数并配置
    gl_VAR.g_totsta, gl_VAR.g_stg, gl_VAR.g_dis = funcs.SET_CONFIG()

    data.CONFIG(nsta=gl_VAR.g_totsta, stg=gl_VAR.g_stg, dis=gl_VAR.g_dis)

    # 初始化data.py中的变量
    SED_LST = data.SED_LST(0, '0' * gl_VAR.g_totsta)
    BUS_CON = data.BUS_CON(0, 0, 0, 0)
    STA_CON = data.STA_CON('0' * gl_VAR.g_totsta, '0' * gl_VAR.g_totsta)

    funcs.OP_C(BUS_CON, STA_CON)
    # 运行
    while True:
        code, instr = funcs.IP_C()
        if code == -2:
            continue
        if code == -1:
            funcs.OP_C_E(STA_CON)
            exit(-1)
        elif code == 0:
            funcs.OP_C(BUS_CON, STA_CON)
            funcs.TIMR()
            funcs.BUS_ACT().BUS_MOV()
        elif code == 1 or code == 2 or code == 3:
            funcs.BUS_ACT().PSG_D()
            funcs.BUS_ACT().PSG_U()
