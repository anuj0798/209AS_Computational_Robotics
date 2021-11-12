import numpy as np

# Tuning parameter
A = 10
ymax = 100
action_space = [-1, 0, 1]
wobble_bit = 1
sensor_bit = 0
crashing_bit = 1


def ext_force(pos):
    return int(A * np.sin(2 * np.pi * pos / ymax))
