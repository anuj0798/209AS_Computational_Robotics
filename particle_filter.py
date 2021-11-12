import numpy as np
pi = 3.14
def p(z,x):
	return exp(-((z - x[0])/(0.5*x[1]))**2/2)/ (0.5*x[1]*sqrt(2*pi))


def particle_filter(X_t_1, u_t, z_t):
	X_t = []
	M = Number_particle
	for m in range(M):
		x_t_1 = X_t_1[m]
		x_t = f(x_t_1, u_t)
		w_t = p(z_t, x_t)

		X_t.append([x_t, w_t])




