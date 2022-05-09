SED_LST = []
tmp_CMD = ()
is_move = 0

class CONFIG:
    TOTAL_STATION = None
    STRATEGY = None
    DISTANCE = None

    def __init__(self, nsta, stg, dis):
        self.TOTAL_STATION = nsta
        self.STRATEGY = stg
        self.DISTANCE = dis
        print('Config:\nTotal_station:', self.TOTAL_STATION, ' Strategy:', self.STRATEGY, ' Distance:', self.DISTANCE)


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
