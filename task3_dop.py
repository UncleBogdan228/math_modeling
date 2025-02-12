import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0,10,frames)
g = 9.8
m = 250000
u = 3000
k = 1000
x0 = 0
vx0 = 0

z0 = x0, vx0

def move_func(z, t):
    x, vx= z
    dx_dt = vx
    dvx_dt = (u * 1000 - m *g)/m
    return dx_dt, dvx_dt

sol = odeint(move_func, z0, t)
fig,ax = plt.subplots()
ball, = plt.plot([],[], 'o', color='r')
ball_line, = plt.plot([],[], '-', color = 'r')

def animate(i):
    ball.set_data([0], [sol[i][0]])
    # ball_line.set_data(sol[:i, 0], sol[:i, 1])

ani = FuncAnimation(fig, animate, frames= frames, interval = 30)

edge = 100
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('task3_dop.gif', writer = "pillow")