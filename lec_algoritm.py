import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#определяем иипеременную
frames = 500
second_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years * second_in_year, frames)

def func (s, t):
    x, vx, y, vy = s
    dx_dt = vx
    dvx_dt = - G * M * x/ (x**2 + y **2) ** 1.5

    dy_dt = vy
    dvy_dt = - G * M * y/ (x**2 + y **2) ** 1.5
    return dx_dt, dvx_dt, dy_dt, dvy_dt

G = 6.67 * 10**(-11)
M = 1.998 * 10**(30)

x0 = 149 * 10 ** 9
vx0 = 0
y0 = 0
vy0 = 30000

s0 = (x0, vx0, y0, vy0)

sol = odeint(func, s0, t)



fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
	
def animate(i):
	
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
	
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
	
 
plt.plot([0], [0], 'o', color = 'y', ms = 20)

edge = 2*x0
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('animation.gif', writer="pillow")