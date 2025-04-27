import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation

# Константы
t = np.linspace(0, 5, 5000)
q = -1.6 * 10 ** -19  # заряд
m = 9.1 * 10 ** -31  # масса электрона
mu = 1.26 * 10 ** -6  # магнитная постоянная
mu_d = 2 * 10 ** 2  # магнитный момент диполя
edge = 300
x_edge = 300


def move_func(s, t):
    x, v_x, y, v_y, z, v_z = s

    r = (x**2 + y**2 + z**2)**(0.5)

    if r < 1 * 10 ** -6:
        Bx = 0
        By = 0
        Bz = 0
    else:
        Bx = 3 * x * z * mu_d * mu / (x**2 + y**2 + z**2)**(5 / 2)
        By = 3 * y * z * mu_d * mu / (x**2 + y**2 + z**2)**(5 / 2)
        Bz = (2 * z**2 - x**2 - y**2) * mu_d * mu / (x**2 + y**2 + z**2)**(5 / 2)

    dxdt = v_x
    dv_xdt = q / m * (v_y * Bz - By * v_z)

    dydt = v_y
    dv_ydt = q / m * (v_z * Bx - Bz * v_x)

    dzdt = v_z
    dv_zdt = q / m * (v_x * By - Bx * v_y)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt


wave_width = 100  # Ширина
wave_height = 100  # Высота
wave_depth = 50 # Глубина (ширина в координате Y)
num_points_x = 10 # Количество точек по x (высоте)
num_points_z = 10 # Количество точек по z (ширине)
num_points_y = 10  # Количество точек по y (глубине)

x_start = -200  # Начальное положение по x
y_offset = 0  # Смещение по оси y вправо
v_x = 300# Скорость "налета" по x
exclusion_radius = 2  # Радиус исключения вокруг (0, 0, 0)

initial_positions = []
for x in np.linspace(-wave_height / 2, wave_height / 2, num_points_x):
    for z in np.linspace(-wave_width / 2, wave_width / 2, num_points_z):
        for y in np.linspace(-wave_depth / 2, wave_depth / 2, num_points_y):  # Добавили цикл по y

                initial_positions.append((x_start, v_x, y, 0, z, 0))

solutions = []
for s0 in initial_positions:
    sol = odeint(move_func, s0, t)
    solutions.append(sol)

x_data = [sol[:, 0] for sol in solutions]
y_data = [sol[:, 2] for sol in solutions]
z_data = [sol[:, 4] for sol in solutions]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([-x_edge, x_edge])
ax.set_ylim([-edge, edge])
ax.set_zlim([-edge, edge])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

balls = []
lines = []
for _ in range(len(solutions)):
    ball, = ax.plot([], [], [], 'o', color='r', markersize=2)
    line, = ax.plot([], [], [], lw=2)
    balls.append(ball)
    lines.append(line)


def init():
    for ball, line in zip(balls, lines):
        ball.set_data([], [])
        ball.set_3d_properties([])
        line.set_data([], [])
        line.set_3d_properties([])
    return tuple(balls + lines)


def update(frame):
    for i in range(len(solutions)):
        balls[i].set_data([x_data[i][frame]], [y_data[i][frame]])
        balls[i].set_3d_properties(z_data[i][frame])

        lines[i].set_data(x_data[i][:frame + 1], y_data[i][:frame + 1])
        lines[i].set_3d_properties(z_data[i][:frame + 1])

    return tuple(balls + lines)

ani = FuncAnimation(fig, update, frames=len(t), interval=1, init_func=init)
#for sol in solutions:
    #ax.plot(sol[:, 0], sol[:, 2], sol[:, 4], alpha=0.3)
ani.save('mnogo2.gif', writer='imagemagick')
#plt.show()