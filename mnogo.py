import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation

# переменная величина
t = np.linspace(0, 4, 4000)

# начальные значения
x0 = 10
v_x0 = 0

y0 = 10
v_y0 = 0

z0 = 10
v_z0 = 10 ** 3

x10 = 20
v_x10 = 0

y10 = 20
v_y10 = 0

z10 = 20
v_z10 = 10 ** 3

s0 = x0, v_x0, y0, v_y0, z0, v_z0, x10, v_x10, y10, v_y10, z10, v_z10
q = 1.6 * 10 ** (-19)  # заряд
m = 9.1 * 10 ** (-31)  # масса электрона
mu = 1.26 * 10 ** (-6)  # магнитная постоянная
mu_d = 2 * 10 ** 2  # магнитный момент диополя
edge = 15


def move_func(s, t):
    x, v_x, y, v_y, z, v_z, x1, v_x1, y1, v_y1, z1, v_z1 = s

    Bx = 3 * x * z * mu_d * mu / (x ** 2 + y ** 2 + z ** 2) ** (5 / 2)
    By = (3 * y * z * mu_d) * mu / (x ** 2 + y ** 2 + z ** 2) ** (5 / 2)
    Bz = (2 * z ** 2 - x ** 2 - y ** 2) * mu_d * mu / (x ** 2 + y ** 2 + z ** 2) ** (5 / 2)

    Bx1 = 3 * x1 * z1 * mu_d * mu / (x1 ** 2 + y1 ** 2 + z1 ** 2) ** (5 / 2)
    By1 = (3 * y1 * z1 * mu_d) * mu / (x1 ** 2 + y1 ** 2 + z1 ** 2) ** (5 / 2)
    Bz1 = (2 * z1 ** 2 - x1 ** 2 - y1 ** 2) * mu_d * mu / (x1 ** 2 + y1 ** 2 + z1 ** 2) ** (5 / 2)

    dxdt = v_x
    dv_xdt = q / m * (v_y1 * Bz - By * v_z1)

    dydt = v_y
    dv_ydt = q / m * (v_z1 * Bx - Bz * v_x1)

    dzdt = v_z
    dv_zdt = q / m * (v_x1 * By - Bx * v_y1)

    dx1dt = v_x
    dv_x1dt = q / m * (v_y1 * Bz1 - By1 * v_z1)

    dy1dt = v_y
    dv_y1dt = q / m * (v_z1 * Bx1 - Bz1 * v_x1)

    dz1dt = v_z
    dv_z1dt = q / m * (v_x1 * By1 - Bx1 * v_y1)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt, dx1dt, dv_x1dt, dy1dt, dv_y1dt, dz1dt, dv_z1dt,


sol = odeint(move_func, s0, t)

x = sol[:, 0]
y = sol[:, 2]
z = sol[:, 4]

x1 = sol[:, 6]
y1 = sol[:, 8]
z1 = sol[:, 10]

fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([-edge, edge])
ax.set_ylim([-edge, edge])
ax.set_zlim([-edge, edge])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")


line, = ax.plot([], [], [])
line1, = ax.plot([], [], [])


def init():
    line.set_data([], [])
    line.set_3d_properties([])

    line1.set_data([], [])
    line1.set_3d_properties([])
    return line, line1,


def update(frame):
    line1.set_data(x1[:frame], y1[:frame])
    line1.set_3d_properties(z1[:frame])

    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line, line1,


ani = FuncAnimation(fig, update, frames=200, interval=1)
ani.save('test1.gif')


