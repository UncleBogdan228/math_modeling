import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)	

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5)= s
	
    dxdt1 = v_x1
    dv_xdt1 = - G * M * x1 / (x1**2 + y1**2)**1.5
	
    dydt1 = v_y1
    dv_ydt1 = - G * M * y1 / (x1**2 + y1**2)**1.5
	
    dxdt2 = v_x2
    dv_xdt2 = - G * M * x2 / (x2**2 + y2**2)**1.5

    dydt2 = v_y2
    dv_ydt2 = - G * M * y2 / (x2**2 + y2**2)**1.5

    dxdt3 = v_x3
    dv_xdt3 = - G * M * x3 / (x3**2 + y3**2)**1.5

    dydt3 = v_y3
    dv_ydt3 = - G * M * y3 / (x3**2 + y3**2)**1.5

    dxdt4 = v_x4
    dv_xdt4 = - G * M * x4 / (x4**2 + y4**2)**1.5

    dydt4 = v_y4
    dv_ydt4 = - G * M * y4 / (x4**2 + y4**2)**1.5

    dxdt5 = v_x5
    dv_xdt5 = - G * M * x5 / (x5**2 + y5**2)**1.5

    dydt5 = v_y5
    dv_ydt5 = - G * M * y5 / (x5**2 + y5**2)**1.5


    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,	
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5)
	
  
	

G = 6.67 * 10**(-11)
M = 1.98 * 10**(30)

x10 = 52 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 42500

x20 = 108 * 10**9
v_x20 = 0
y20 = 0
v_y20 = 35000

x30 = 148 * 10**9
v_x30 = 0
y30 = 0
v_y30 = 29765

x40 = 228 * 10**9
v_x40 = 0
y40 = 0
v_y40 = 24130

x50 = 21 * 10**9
v_x50 = 0
y50 = 0
v_y50 = 20122




s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50)
	
sol = odeint(move_func, s0, t)
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
	
ball2, = plt.plot([], [], 'o', color='b')
ball_line2, = plt.plot([], [], '-', color='b')

ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')

ball4, = plt.plot([], [], 'o', color='y')
ball_line4, = plt.plot([], [], '-', color='y')

ball5, = plt.plot([], [], 'o', color='c')
ball_line5, = plt.plot([], [], '-', color='c')

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
	
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
	
 
plt.plot([0], [0], 'o', color = 'y', ms = 20)

edge = 2*x40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('task1.gif', writer="pillow")