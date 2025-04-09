import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

# Константы
mu_0 = 1.26 * 10 ** (-6)  
mu_d = 200 
edge = 30

def move_func (x, y, z, mu=mu_d, mu_00=mu_0):

    r = np.sqrt(x**2 + y**2 + z**2)
    if r < 1e-6:
        return np.array([0, 0, 0])

    m = mu*mu_00 

    B_x = (3 * m * x * z) / (4 * np.pi * r**5)
    B_y = (3 * m * y * z) / (4 * np.pi * r**5)
    B_z = (m * (3 * z**2 - r**2)) / (4 * np.pi * r**5)

    return np.array([B_x, B_y, B_z])


def field_lines(x_start, y_start, z_start, step_size=0.5, max_steps=200):

    x = [x_start]
    y = [y_start]
    z = [z_start]

    for i in range(max_steps):
        B = move_func(x[-1], y[-1], z[-1])
        B_norm = B / np.linalg.norm(B)  # Нормируем вектор поля
        x.append(x[-1] + step_size * B_norm[0])
        y.append(y[-1] + step_size * B_norm[1])
        z.append(z[-1] + step_size * B_norm[2])

    return x, y, z

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')


ax.set_xlim([-edge, edge])
ax.set_ylim([-edge, edge])
ax.set_zlim([-edge, edge])


num_lines = 20
start_range = np.linspace(-edge,edge, num_lines)


for x_start in start_range:
    for y_start in start_range:
        # Задаем начальную точку и генерируем линии поля
        x, y, z = field_lines(x_start, y_start, 5) 
        ax.plot(x, y, z, color='deepskyblue', linewidth=0.7)

        x, y, z = field_lines(x_start, y_start, -5)  
        ax.plot(x, y, z, color='deepskyblue', linewidth=0.7)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title("Линии магнитного поля диполя")


plt.savefig("field_lines.png")


