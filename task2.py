import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
t = np.linspace(0, 1, frames)	

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6)= s
	
    dxdt1 = v_x1
    dv_xdt1 = (k * q1 * Q * x1)/ (x1**2 + y1**2)**1.5 / m
	
    dydt1 = v_y1
    dv_ydt1 = (k * q1 * Q * y1)/ (x1**2 + y1**2)**1.5 / m
	
    dxdt2 = v_x2
    dv_xdt2 = (k * q2 * Q * x2)/(x2**2 + y2**2)**1.5 / m

    dydt2 = v_y2
    dv_ydt2 = (k * q2 * Q * y2)/(x2**2 + y2**2)**1.5 /  m

    dxdt3 = v_x3
    dv_xdt3 = (k * q3 * Q * x3)/ (x3**2 + y3**2)**1.5 / m 

    dydt3 = v_y3
    dv_ydt3 = (k * q3 * Q * y3)/ (x3**2 + y3**2)**1.5 / m

    dxdt4 = v_x4
    dv_xdt4 = (k * q4 * Q * x4)/ (x4**2 + y4**2)**1.5 / m

    dydt4 = v_y4
    dv_ydt4 = (k * q4 * Q * y4)/ (x4**2 + y4**2)**1.5 / m 

    dxdt5 = v_x5
    dv_xdt5 = (k * q5 * Q * x5)/ (x5**2 + y5**2)**1.5 / m

    dydt5 = v_y5
    dv_ydt5 = (k * q5 * Q * y5)/ (x5**2 + y5**2)**1.5 / m

    dxdt6 = v_x6
    dv_xdt6 = (k * q6 * Q * x6)/ (x6**2 + y6**2)**1.5 / m

    dydt6 = v_y6
    dv_ydt6 = (k * q6 * Q * y6)/ (x6**2 + y6**2)**1.5 / m


    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,	
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5,
            dxdt6, dv_xdt6, dydt6, dv_ydt6)
	
  
	

k = 9 * 10 ** 9
m = 0.1
Q = 50 * 10 ** - 3

q1 = 3 * 10 ** -4
x10 = -30
v_x10 = 100
y10 = 15
v_y10 = 0

q2 = -3 * 10 ** -4
x20 = -30
v_x20 = 100
y20 = 10
v_y20 = 0

q3 = 2 * 10 ** -4
x30 = -30
v_x30 = 100
y30 = 5
v_y30 = 0

q4 = -2 * 10 ** - 4
x40 = -30
v_x40 = 100
y40 = - 5
v_y40 = 0

q5 = 1 * 10 ** -4
x50 = -30
v_x50 = 100
y50 = - 10
v_y50 = 0

q6 = -1 * 10 ** -4
x60 = -30
v_x60 = 100
y60 = -15
v_y60 = 0



s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60)
	
sol = odeint(move_func, s0, t)
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
	
ball2, = plt.plot([], [], 'o', color='orange')
ball_line2, = plt.plot([], [], '-', color='orange')

ball3, = plt.plot([], [], 'o', color='yellow')
ball_line3, = plt.plot([], [], '-', color='yellow')

ball4, = plt.plot([], [], 'o', color='g')
ball_line4, = plt.plot([], [], '-', color='g')

ball5, = plt.plot([], [], 'o', color='b')
ball_line5, = plt.plot([], [], '-', color='b')

ball6, = plt.plot([], [], 'o', color='purple')
ball_line6, = plt.plot([], [], '-', color='purple')

def animate(i):
	
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
    
    ball2.set_data([sol[i][4]], [sol[i][6]])
    ball_line2.set_data(sol[:i, 4], sol[:i, 6])

    ball3.set_data([sol[i][8]], [sol[i][10]])
    ball_line3.set_data(sol[:i, 8], sol[:i, 10])

    ball4.set_data([sol[i][12]], [sol[i][14]])
    ball_line4.set_data(sol[:i, 12], sol[:i, 14])

    ball5.set_data([sol[i][16]], [sol[i][18]])
    ball_line5.set_data(sol[:i, 16], sol[:i, 18])

    ball6.set_data([sol[i][20]], [sol[i][22]])
    ball_line6.set_data(sol[:i, 20], sol[:i, 22])
	
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
	
 
plt.plot([0], [0], 'o', color = 'y', ms = 20)

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('task2.gif', writer="pillow")