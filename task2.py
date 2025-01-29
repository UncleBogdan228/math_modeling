import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1 ,0.001)
x0 = 5
y0 = -7
z0 = x0, y0
e = 2.72

def diff_func(z, t): 
    x, y = z

    dx_dt = 3*x - 2*y + (e ** (3 * t)) / (e ** t + 1 )
    dy_dt = x - (e ** (3 * t)) / (e ** t + 1 )

    return dx_dt, dy_dt

sol = odeint(diff_func, z0, t)

plt.plot(t, sol)
plt.savefig('task2')

