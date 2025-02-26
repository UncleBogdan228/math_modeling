import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
t = np.linspace(0, 1, frames)	

def move_func(s, t):
    (x1, v_x1, y1, v_y1)= s
	
    dxdt1 = v_x1
    dv_xdt1 = (k * q1 * Q * x1)/ (x1**2 + y1**2)**1.5 / m
    dydt1 = v_y1
    dv_ydt1 = (k * q1 * Q * y1)/ (x1**2 + y1**2)**1.5 / m
	


    return (dxdt1, dv_xdt1, dydt1, dv_ydt1)
	
  
	

k = 9 * 10 ** 9
Q = 5 * 10 ** - 3

m = 0.1
q1 = -3 * 10 ** -4

x10 = -30
v_x10 = 100
y10 = 10
v_y10 = 0


s0 = (x10, v_x10, y10, v_y10)
	
sol = odeint(move_func, s0, t)
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
	
def animate(i):
	
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
	
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
	
 
plt.plot([0], [0], 'o', color = 'y', ms = 20)

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('task2.gif', writer="pillow")