import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0,5,frames)
g = 9.8
x0 = 0
vx0 = 0.5
m = 0.8
k = 500



z0 = x0, vx0

def move_func(z,t,g,k,m):
    x, vx= z
    dx_dt = vx
    dvx_dt = g - k*x/m
    return dx_dt, dvx_dt

sol = odeint(move_func, z0, t, args = (g, k, m))
fig,ax = plt.subplots()
ball, = plt.plot([],[], 'o', color='r')
ball_line, = plt.plot([],[], '-', color = 'r')

def animate(i):
    ball.set_data([sol[i][0]], [sol[i][1]])
    ball_line.set_data(sol[:i, 0], sol[:i, 1])

ani = FuncAnimation(fig, animate, frames= frames, interval = 30)

edge = 0.5
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
ani.save('task4.gif', writer = "pillow")