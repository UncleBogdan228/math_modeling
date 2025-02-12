import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 1000
t = np.linspace(0,10,frames)
g = 9.8
x0 = 0.08
vx0 = 0.5
m = 0.5
k = 125
w = 5



z0 = x0, vx0

def move_func(z, t):
    x, vx= z
    dx_dt = vx
    dvx_dt = - (k/m) * x - g + 5 * np.cos(w * t)
    return dx_dt, dvx_dt

sol = odeint(move_func, z0, t)
fig,ax = plt.subplots()
ball, = plt.plot([],[], 'o', color='r')
ball_line, = plt.plot([],[], '-', color = 'r')

def animate(i):
    ball.set_data([0], [sol[i][0]])
    # ball_line.set_data(sol[:i, 0], sol[:i, 1])

ani = FuncAnimation(fig, animate, frames= frames, interval = 30)

edge = 0.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('task2_v_dop.gif', writer = "pillow")