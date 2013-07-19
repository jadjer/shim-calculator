class Shim(object):
    def __init__(self, shim_set, shim_num, shim_th, source_v, dest_v):
        self.shim_set = shim_set
        self.shim_num = shim_num
        self.shim_th = shim_th
        self.source_v = source_v
        self.dest_v = dest_v

    def get_nearest_shim_num(self, shim_th):
        shim_n = '000'
        return shim_n


class Valve(object):
    def __init__(self, norm_clr, clr, dev_clr, inst_shim, v_type, v_num):
        self.norm_clr = norm_clr
        self.clr = clr
        self.dev_clr = dev_clr
        self.inst_shim = inst_shim
        self.v_type = v_type
        self.v_num = v_num


class Cylinder(object):
    def __init__(self, v_per_cyl, c_type, c_num):
        self.valve_list = []
        self.v_per_cyl = v_per_cyl
        self.c_type = c_type
        self.c_num = c_num

    def add_valve(self, valve):
        self.valve_list.append(valve)


class Engine(object):
    def __init__(self, engine_type):
        self.cyl_list = []
        self.engine_type = engine_type

    def add_cylinder(self, cylinder):
        self.cyl_list.append(cylinder)

    def get_valve_list(self):
        v_l = []
        for y in self.cyl_list:  # all cylinders
            for x in y.valve_list:  # all valves in each cyl
                v_l.append(x)
        return v_l

    def get_out_of_norm_valve_list(self):
        res_l = []
        v_l = self.get_valve_list()
        for x in v_l:
            if abs(x.clr - x.norm_clr) > x.dev_clr:
                res_l.append(x)
        return res_l


# Temporary definitions for main parameters
engine_types = ['1', '2-P', '2-V', '3R', '4R', '4V-N', '4V-U', '4V-P']
cylinder_types = ['2EI', '4EI', '4IE', '4EIL', '4EIR', '4IEL', '4IER', '5EI']
norm_clr_ex = 0.20
norm_clr_in = 0.15
dev_clr_ex = 0.03
dev_clr_in = 0.03
# Temporary definitions for main parameters

e = Engine('4R')

for i in range(4):
    c = Cylinder(4, '4EI', i + 1)

    v = Valve(0.20, 0.25, 0.03, Shim([2.225, 2.250], '222', 2.225 + i * 0.01, 1, 1), 'ex', i * 4 + 1)
    c.add_valve(v)
    v = Valve(0.20, 0.20, 0.03, Shim([2.225, 2.250], '225', 2.250 + i * 0.01, 1, 1), 'ex', i * 4 + 2)
    c.add_valve(v)
    v = Valve(0.15, 0.11, 0.03, Shim([2.225, 2.250], '222', 2.225 - i * 0.01, 1, 1), 'in', i * 4 + 3)
    c.add_valve(v)
    v = Valve(0.15, 0.15, 0.03, Shim([2.225, 2.250], '225', 2.250 - i * 0.01, 1, 1), 'in', i * 4 + 4)
    c.add_valve(v)
    e.add_cylinder(c)

valve_list = e.get_valve_list()  # make list for testing purposes
for x in valve_list:
    print x.inst_shim.shim_th, x.v_type, x.v_num

valve_list = e.get_out_of_norm_valve_list()
for x in valve_list:
    print x.clr, x.norm_clr, x.v_type, x.v_num

engine_types = ['1', '2-P', '2-V', '3R', '4R', '4V-N', '4V-U', '4V-P']
cylinder_types = ['2EI', '4EI', '4IE', '4EIL', '4EIR', '4IEL', '4IER', '5EI']
norm_clr_ex = 0.20
norm_clr_in = 0.15
dev_clr_ex = 0.03
dev_clr_in = 0.03













# f = open('data\\Honda_748.txt', 'r')
# a = []
# for line in f:
#     a = line.split(' : ')
#     print a[0], a[1][:-1:]
