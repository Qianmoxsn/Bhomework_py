import funcs
import data

if __name__ == '__main__':
    # 输入配置参数并配置
    nsta, stg, dis = funcs.SET_CONFIG()
    data.CONFIG(nsta=nsta, stg=stg, dis=dis)
    # 初始化
    funcs.INIT()
    funcs.OP_C()
    # 运行
    while True:
        code, instr = funcs.IP_C()
        if code == '-1':
            funcs.OP_C_E()
            exit(-1)
        elif code == '0':
            funcs.OP_C()
            funcs.TIMR()
            funcs.BUS_ACT().BUS_MOV()
        elif code == '1' or code == '2' or code == '3':
            funcs.BUS_ACT().PSG_D()
            funcs.BUS_ACT().PSG_U()
