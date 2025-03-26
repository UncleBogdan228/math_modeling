import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation

#переменная величина
t = np.linspace (0, 4, 4000)

#начальные значения
x0 = 10
v_x0 = 0
 
y0 = 20
v_y0 = -10

z0 = 0
v_z0 = 10**3

#2 начальные значения
x10 = 5
v_x10 = 0
 
y10 = 30
v_y10 = -10

z10 = 0
v_z10 = 10**3

s0 = x0, v_x0, y0, v_y0, z0, v_z0
s01 = x10, v_x10, y10, v_y10, z10, v_z10

q = 1.6 * 10 ** (-19) #заряд
m = 9.1 * 10 ** (-31) #масса электрона
mu = 1.26 * 10 ** (-6) #магнитная постоянная
mu_d = 2 * 10 ** 2 #магнитный момент диополя
edge = 15

def move_func (s, t):
    x, v_x, y, v_y, z, v_z = s

    Bx = 3 * x * z * mu_d * mu / (x**2 + y**2 + z**2) ** (5/2)
    By = (3 * y * z * mu_d) * mu / (x**2 + y**2 + z**2) ** (5/2)
    Bz = (2 * z**2 - x**2 - y**2) * mu_d * mu / (x**2 + y**2 + z**2) ** (5/2)
    
    dxdt = v_x
    dv_xdt = q / m * (v_y * Bz - By * v_z)

    dydt = v_y
    dv_ydt = q / m * (v_z * Bx - Bz * v_x)

    dzdt = v_z
    dv_zdt = q / m * (v_x * By - Bx * v_y)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

sol = odeint(move_func, s0, t)
sol1 = odeint(move_func, s01, t)

x = sol[:, 0]
y = sol[:, 2]
z = sol[:, 4]

x1 = sol1[:, 0]
y1 = sol1[:, 2]
z1 = sol1[:, 4]

fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([-edge, edge])
ax.set_ylim([-edge, edge])
ax.set_zlim([-edge, edge])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ball, = plt.plot([], [], [], 'o', color='r')
line, = ax.plot([], [], [], 'o', lw=2)

ball1, = plt.plot([], [], [], 'o', color='r')
line1, = ax.plot([], [], [], 'o', lw=2)

def init():
    ball.set_data([], [])
    ball.set_3d_properties([])

    line.set_data([], [])
    line.set_3d_properties([])

    ball1.set_data([], [])
    ball1.set_3d_properties([])

    line1.set_data([], [])
    line1.set_3d_properties([])
    return ball, line, ball1, line1, 


def update(frame):
    ball.set_data([x[frame]], [y[frame]])
    ball.set_3d_properties(z[frame])
    
    line.set_data([x[frame]], [y[frame]])
    line.set_3d_properties(z[frame])

    ball1.set_data([x1[frame]], [y1[frame]])
    ball1.set_3d_properties(z1[frame])
    
    line1.set_data([x1[frame]], [y1[frame]])
    line1.set_3d_properties(z1[frame])
    return ball, line, ball1, line1, 

ax.plot(sol[:, 0], sol [:, 2], sol [:, 4])
ax.plot(sol1[:, 0], sol1 [:, 2], sol1 [:, 4])
ani = FuncAnimation(fig, update, frames=200, interval=1)
ani.save('mnogo.gif')

