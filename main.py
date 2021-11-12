from particle_model import particle_dt_cs
import matplotlib.pyplot as plt
import numpy as np
from pynput import keyboard
import keyboard
import time


# Inputs to the system (External and applied)
def ext_force(pos):
    return 2 * np.sin(pos)


def get_input(inc):
    global input_force
    input_force += inc
    if input_force > 1:
        input_force = 1
    elif input_force < -1:
        input_force = -1
    return input_force


if __name__ == '__main__':

    particle_dynamics = particle_dt_cs(mass=1, vmax=5, pc=0.1, y0=0, v0=0, t0=0)
    states_pos = list()
    states_vel = list()
    outputs = list()
    input_force = 0

    while particle_dynamics.t < 100:
        if keyboard.read_key() == "a":
            input_force = get_input(-0.1)
        if keyboard.read_key() == "d":
            input_force = get_input(0.1)
        if keyboard.read_key() == "s":
            break

        print(input_force)
        particle_dynamics.run(input_force, ext_force(particle_dynamics.x[0]))
        states_pos.append(particle_dynamics.x[0])
        states_vel.append(particle_dynamics.x[1])
        outputs.append(particle_dynamics.z)
        time.sleep(0.1)

    plt.plot(states_pos, label="y[t]")
    plt.plot(outputs, label="z[t]")
    plt.plot(states_vel, label="v[t]")
    plt.legend()
    plt.xlabel("Time t")
    plt.show()
