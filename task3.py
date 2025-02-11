import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0,5,frames)
a0 = 100
k1 = 0.3
k2 = 0.5
x0 = 0
y0 = 0

z0 = x0, y0

def move_func(z, t, k1, k2, a0):
    x, y = z
    dx_dt = k1*(a0 - x - y)
    
    dy_dt = k2*(a0 - x - y) 
    return dx_dt, dy_dt

sol = odeint(move_func, z0, t, args = (k1, k2, a0))
fig,ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r') 
ball_line, = plt.plot([], [], '-', color='r')

ball2, = plt.plot([], [], 'o', color='b') 
ball_line2, = plt.plot([], [], '-', color='b')

def animate(i):
    ball.set_data([sol[i][0]], [a0/2])  
    ball_line.set_data(sol[:i, 0], [a0/2]*i) 
    ball2.set_data([sol[i][1]], [a0/4]) 
    ball_line2.set_data(sol[:i, 1], [a0/4]*i )  

ani = FuncAnimation(fig, animate, frames= frames, interval = 30)

edge = 100
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
ani.save('task3.gif', writer = "pillow")