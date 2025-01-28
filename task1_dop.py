import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

V = 500
G = 6.67 * 10**(-11)
r = 637100
M = 5.9722 * 10**24
t = np.arange(0, 10, 0.1)
sp = []
count = 0


def model(V, t, G):
    dSdt = M * G / V * r ** 2
    if V > count:
        sp.append(V)

    return dSdt


N = odeint(model, M, t, args=(V,))
print('Скорость в момент столкновения:', *max(sp))
plt.figure(figsize=(10, 5))
plt.plot(t, N)
plt.savefig('task1_dop.png')