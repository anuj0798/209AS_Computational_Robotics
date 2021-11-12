import numpy as np
import matplotlib.pyplot as plt


# TODO
# Private variable
# matplotlib keyboard/ pynput input for simulator ( remove keyboard) https://matplotlib.org/stable/gallery/event_handling/keypress_demo.html
# visualization (Realtime simulator matplotlib) https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time
# look at probablity of crashing in dtcs and remove self.v
# define tp in dtds
# improve code using Anwesha's and Alex's github code
# note for different probablity functions

class particle_dt_cs:
    """Particle on a numberline in discrete time and continuous space"""

    def __init__(self, mass, vmax, pc, y0, v0, t0, wobble_bit, sensor_bit, crash_bit):
        self.mass = mass
        self.vmax = vmax
        self.pc = pc
        self.y = y0
        self.v = v0
        self.x = (self.y, self.v)
        self.t = t0
        self.z = 0
        self.wobble_bit = wobble_bit
        self.sensor_bit = sensor_bit
        self.crash_bit = crash_bit

    def u(self, input_force):
        return input_force

    def wobble_noise(self):
        if self.wobble_bit:
            sigma_d = (0.1 * self.x[1]) ** 2
            return np.random.normal(0, sigma_d)
        else:
            return 0

    def sensor_noise(self):
        if self.sensor_bit:
            sigma_n = (0.5 * self.x[1]) ** 2
            return np.random.normal(0, sigma_n)
        else:
            return 0

    def calc_pos(self):
        self.y = self.x[0] + self.x[1]

    def calc_vel(self):
        if self.crash_bit:
            if np.random.random() <= 1 - (abs(self.v - self.vmax) * self.pc / self.vmax):
                self.v = self.x[1] + (1 / self.mass) * (self.u(input_force) - ext_force) + self.wobble_noise()
            else:
                self.v = 0
        else:
            self.v = self.x[1] + (1 / self.mass) * (self.u(input_force) - ext_force) + self.wobble_noise()

    def state_equation(self, input_force, ext_force):
        self.calc_pos()
        self.calc_vel()
        return self.y, self.v

    def output_equation(self):
        return self.x[0] + self.sensor_noise()

    def run(self, input_force, ext_force):
        self.x = self.state_equation(input_force, ext_force)
        self.z = self.output_equation()
        self.t += 1


class particle_dt_ds:
    """Particle on a numberline in discrete time and discrete space"""

    def __init__(self, mass, vmax, ymax, action_space, ext_force, pw, pc, gamma, y0, v0, t0, wobble_bit, sensor_bit,
                 crash_bit):

        self.mass = mass
        self.vmax = vmax
        self.ymax = ymax
        self.y_list = [*range(-self.ymax, self.ymax + 1, 1)]
        self.v_list = [*range(-self.vmax, self.vmax + 1, 1)]
        self.S = list()
        self.A = action_space
        self.P = dict()
        self.gamma = gamma
        self.ext_force = ext_force
        self.pw = pw
        self.wobble_bit = wobble_bit
        self.sensor_bit = sensor_bit
        self.crash_bit = crash_bit
        self.pc = pc
        self.y = y0
        self.v = v0
        self.x = (self.y, self.v)
        self.t = t0
        self.z = 0

    def state_space_s(self):
        for y in self.y_list:
            for v in self.v_list:
                self.S.append((y, v))

    def transition_probability_p(self):
        for s in self.S:
            for a in self.A:
                for s_new in self.S:
                    if s_new[2] == 0:
                        tp = self.pc*abs(s[2])/self.vmax
                    else:
                        tp = (1 - (self.pc*abs(s[2])/self.vmax)) * normal_distribution


                    self.P.update({(s, a, s_new): tp})


    def wobble_noise(self):
        if self.wobble_bit:
            prob = np.random.random()
            if prob <= (self.x[1] / self.vmax) * self.pw / 2:
                return 1
            elif (self.x[1] / self.vmax) * self.pw / 2 < prob <= (self.x[1] / self.vmax) * self.pw:
                return 0
            else:
                return -1

        else:
            return 0

    def sensor_noise(self):
        if self.sensor_bit:
            sigma_n = (0.5 * self.x[1]) ** 2
            return np.random.normal(0, sigma_n)
        else:
            return 0

    def calc_pos(self):
        self.y = self.x[0] + self.x[1]

    def calc_vel(self):
        if self.crash_bit:
            if np.random.random() <= 1 - (abs(self.x[1]) * self.pc / self.vmax):
                self.v = self.x[1] + (1 / self.mass) * (self.u(input_force) - ext_force) + self.wobble_noise()
            else:
                self.v = 0
        else:
            self.v = self.x[1] + (1 / self.mass) * (self.u(input_force) - ext_force) + self.wobble_noise()

    def u(self, input_force):
        return input_force

    def state_equation(self, input_force, ext_force):
        self.calc_pos()
        self.calc_vel()
        return self.y, self.v

    def output_equation(self):
        return self.x[0] + self.sensor_noise()

    def run(self, input_force, ext_force):
        self.x = self.state_equation(input_force, ext_force)
        self.z = self.output_equation()
        self.t += 1

# class particle_dt_ds:
#     def __init__(self, mass, vmax, ymax, pc, pw y0, v0, t0):


#         self.pw = pw
#
#         self.pc = pc
#         self.y = y0
#         self.v = v0
#         self.x = (self.y, self.v)
#         self.t = t0
#         self.z = 0
#
#     def wobble_noise(self):
#         if np.random.random() <= (self.x[1]/ vmax) * self.pw /2
#         sigma_d = (0.1 * self.x[1]) ** 2
#         return np.random.normal(0, sigma_d)
