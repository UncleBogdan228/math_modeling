import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0,20,frames)
a0 = 500
b0 = 0
c0 = 0
k1 = 0.5
k2 = 0.8
k3 = 0.7
z0 = a0, b0, c0

def move_func(z, t, k1, k2, k3):
    a, b, c = z
    da_dt = - k1 * a
    db_dt = k1 * a - k2 * b
    dc_dt = k2 * b - k3 * c
    return da_dt, db_dt, dc_dt

sol = odeint(move_func, z0, t, args = (k1, k2, k3))
fig,ax = plt.subplots()
A_line, = plt.plot([],[], '-', color = 'r')
B_line, = plt.plot([],[], '-', color = 'b')
C_line, = plt.plot([],[], '-', color = 'y')


def animate(i):
    A_line.set_data(sol[:i, 0], sol[:i, 0])
    B_line.set_data(sol[:i, 0], sol[:i, 1])
    C_line.set_data(sol[:i, 0], sol[:i, 2])

ani = FuncAnimation(fig, animate, frames= frames, interval = 30)

edge = 500
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
ani.save('task1_dop.gif', writer = "pillow")