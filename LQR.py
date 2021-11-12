import numpy as np
import matplotlib.pyplot as plt



A = np.array([[1, 1],
              [0, 1]])

B = np.array([[0, 0],
              [0, 1]])

yin = 5
vin = 2

x = np.array([[yin],
              [vin]])

Q
R
N

Pk = Q

Pk_1 = A.T@Pk@A - (A.T@Pk@B + N) @ (np.linalg.inv(R + B.T@Pk@B)) @ (B.T@Pk@A + N.T) + Q