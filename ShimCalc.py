class Valve(object):
    def __init__(self, norm_clr, clr, high_clr, low_clr, inst_shim, shim_set, v_type):
        self.norm_clr = norm_clr
        self.clr = clr
        self.high_clr = high_clr
        self.low_clr = low_clr
        self.inst_shim = inst_shim
        self.shim_set = shim_set
        self.v_type = v_type


class Cylinder(object):
    def __init__(self, v_per_cyl, c_type):
        self.valve_list = []
        self.v_per_cyl = v_per_cyl
        self.c_type = c_type

    def add_valve(self, valve):
        self.valve_list.append(valve)


class Engine(object):
    def __init__(self, engine_type):
        self.cyl_list = []
        self.engine_type = engine_type

    def add_cylinder(self, cylinder):
        self.cyl_list.append(cylinder)

e = Engine('Inline-4')

for i in range(4):
    c = Cylinder(4, 'e-fr')
    v = Valve(0.03, 0.03, 0.033, 0.027, 2.225 + i * 0.01, [2.225, 2.250], 'in')
    c.add_valve(v)
    v = Valve(0.03, 0.03, 0.033, 0.027, 2.225 - i * 0.01, [2.225, 2.250], 'in')
    c.add_valve(v)
    v = Valve(0.03, 0.03, 0.033, 0.027, 2.225 - i * 0.01, [2.225, 2.250], 'ex')
    c.add_valve(v)
    v = Valve(0.03, 0.03, 0.033, 0.027, 2.225 + i * 0.01, [2.225, 2.250], 'ex')
    c.add_valve(v)
    e.add_cylinder(c)

for y in e.cyl_list:
    for x in y.valve_list:
        print x.inst_shim, x.v_type














# f = open('data\\Honda_748.txt', 'r')
# a = []
# for line in f:
#     a = line.split(' : ')
#     print a[0], a[1][:-1:]
