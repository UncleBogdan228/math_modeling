import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5 ,0.01)
y0 = 3
k0 = 0
z0 = k0, y0

def diff_func(z, t): 
    k, y = z

    dk_dt = np.sin(t) + np.cos(t)
    dy_dt = k 

    return dk_dt, dy_dt

sol = odeint(diff_func, z0, t)

plt.plot(t, sol)
plt.savefig('task3')