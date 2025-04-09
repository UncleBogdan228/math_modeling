import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation

# Константы
t = np.linspace(0, 5, 5000)
q = -1.6 * 10 ** -19  # заряд электрона (отрицательный)
m = 9.1 * 10 ** -31  # масса электрона
mu = 1.26 * 10 ** -6  # магнитная постоянная (можно не использовать явно)
mu_d = 7.94 * 10 ** 22  # Магнитный момент диполя Земли (А*м^2) - подберите значение!
R_earth = 6.371 * 10 ** 6  # Радиус Земли (м) - можно использовать для масштабирования

edge = 20 * 10 ** 6 # Увеличьте масштаб для отображения
x_edge = 15 * 10 ** 6 # Увеличьте масштаб для отображения

def magnetic_field(x, y, z):

    r = np.sqrt(x**2 + y**2 + z**2)

    if r < 1e3:  # Избегаем деления на ноль вблизи диполя
        return np.array([0, 0, 0])

    Bx = 3 * mu * mu_d * x * z / (4 * np.pi * r**5)
    By = 3 * mu * mu_d * y * z / (4 * np.pi * r**5)
    Bz = mu * mu_d * (2 * z**2 - x**2 - y**2) / (4 * np.pi * r**5)

    return np.array([Bx, By, Bz])


def move_func(s, t):

    x, v_x, y, v_y, z, v_z = s

    B = magnetic_field(x, y, z)
    Bx, By, Bz = B

    dxdt = v_x
    dv_xdt = q / m * (v_y * Bz - v_z * By)

    dydt = v_y
    dv_ydt = q / m * (v_z * Bx - v_x * Bz)

    dzdt = v_z
    dv_zdt = q / m * (v_x * By - v_y * Bx)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt


wave_width = 1 * 10 ** 6  # Ширина начального пучка
wave_height = 1 * 10 ** 6 # Высота начального пучка
wave_depth = 5 * 10 ** 6
num_points_z = 10
num_points_x = 10  # Количество точек по x
num_points_y = 5 # Количество точек по y
x_start = 15 * 10 ** 6  # Начальное положение по x (далеко от Земли)
y_offset = 0  # Смещение по оси y вправо
v_x = 0.1  # Скорость "налета" по x


# Генерация начальных положений
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


u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
earth_x = R_earth * np.outer(np.cos(u), np.sin(v))
earth_y = R_earth * np.outer(np.sin(u), np.sin(v))
earth_z = R_earth * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(earth_x, earth_y, earth_z, color="blue", alpha=0.5)


balls = []
lines = []
for _ in range(len(solutions)):
    ball, = ax.plot([], [], [], 'o', color='r', markersize=2)
    line, = ax.plot([], [], [], lw=1, alpha=0.5)  # Уменьшим толщину линий
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


for sol in solutions:
    ax.plot(sol[:, 0], sol[:, 2], sol[:, 4], alpha=0.3)  # Закомментировано

ani = FuncAnimation(fig, update, frames=len(t), interval=1, init_func=init)
#ani.save('earth_electrons.gif', writer='imagemagick')
plt.show()
