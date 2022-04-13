class CONFIG:
    def __init__(self, nsta, stg, dis):
        self.TOTAL_STATION = nsta
        self.STRATEGY = stg
        self.DISTANCE = dis


class SED_LST:
    def __init__(self, sgm, sta_num):
        self.sgm = sgm
        self.sta_num = sta_num


class BUS_CON:
    def __init__(self, dric, station, move, dest):
        self.dric = dric
        self.station = station
        self.move = move
        self.dest = dest


class STA_CON:
    def __init__(self, cw_station, ccw_station):
        self.cw_station = cw_station
        self.ccw_station = ccw_station
