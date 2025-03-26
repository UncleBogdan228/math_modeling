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

y0 = 20
v_y0 = -10

z0 = 0
v_z0 = 30

# 2 начальные значения
x10 = 5
v_x10 = 0

y10 = 30
v_y10 = -10

z10 = 0
v_z10 = 30

s0 = [(x0, v_x0, y0, v_y0, z0, v_z0), (), ()]
s01 = x10, v_x10, y10, v_y10, z10, v_z10

q = 1.6 * 10 ** (-19)  # заряд
m = 9.1 * 10 ** (-31)  # масса электрона
mu = 1.26 * 10 ** (-6)  # магнитная постоянная
mu_d = 2 * 10 ** 2  # магнитный момент диополя
edge = 15


def move_func(s, t):
    x, v_x, y, v_y, z, v_z = s

    Bx = 3 * x * z * mu_d * mu / (x ** 2 + y ** 2 + z ** 2) ** (5 / 2)
    By = (3 * y * z * mu_d) * mu / (x ** 2 + y ** 2 + z ** 2) ** (5 / 2)
    Bz = (2 * z ** 2 - x ** 2 - y ** 2) * mu_d * mu / (x ** 2 + y ** 2 + z ** 2) ** (5 / 2)

    dxdt = v_x
    dv_xdt = q / m * (v_y * Bz - By * v_z)

    dydt = v_y
    dv_ydt = q / m * (v_z * Bx - Bz * v_x)

    dzdt = v_z
    dv_zdt = q / m * (v_x * By - Bx * v_y)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

output = []
for s in s0:
    sol = odeint(move_func, s, t)
    output.append(sol)

x = sol[:, 0]
y = sol[:, 2]
z = sol[:, 4]


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
balls = [plt.plot([], [], [], 'o', color='r') for _ in range(len(output))]
ball, = plt.plot([], [], [], 'o', color='r')
line, = ax.plot([], [], [], 'o', lw=2)
for i in range(0, 1):
    sol = odeint(move_func, s0[i], t)
    x[i] = sol[:, 0]
    y[i] = sol[:, 2]
    z[i] = sol[:, 4]




    ax.set_xlim([-edge, edge])
    ax.set_ylim([-edge, edge])
    ax.set_zlim([-edge, edge])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ball[i], = plt.plot([], [], [], 'o', color='r')
    line[i], = ax.plot([], [], [], 'o', lw=2)


    def init():
        ball[i].set_data([], [])
        ball[i].set_3d_properties([])

        line[i].set_data([], [])
        line[i].set_3d_properties([])
        return line[i],


    def update(frame):
        ball[i].set_data(output[i][:, 0], output[i][:, 2])
        ball[i].set_data(output[0][x[i][frame]], [y[i][frame]])
        ball[i].set_3d_properties(output[i][:, 4])

        line[i].set_data([x[i][frame]], [y[i][frame]])
        line[i].set_3d_properties(z[i][frame])

        ball[i].set_data([x[i][frame]], [y[i][frame]])
        ball[i].set_3d_properties(z[i][frame])

        line[i].set_data([x[i][frame]], [y[i][frame]])
        line[i].set_3d_properties(z[i][frame])
        return line[i],


    ax.plot(sol[i][:, 0], sol[i][:, 2], sol[i][:, 4])

    ani = FuncAnimation(fig, update, frames=200, interval=1)
    plt.show()

