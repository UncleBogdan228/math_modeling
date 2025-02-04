import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0.1, 5 ,0.001)
y0 = 3
k0 = 0
z0 = k0, y0

def diff_func(z, t): 
    k, y = z

    dk_dt = (-t*k - (4*t**2 + 0.5**2)*y)/t**2
    dy_dt = k 

    return dk_dt, dy_dt

sol = odeint(diff_func, z0, t)

plt.plot(t, sol)
plt.savefig('task4_dop.png')