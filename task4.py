import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5 ,0.01)
y0 = 4
k0 = -1
z0 = k0, y0

def diff_func(z, t): 
    k, y = z

    dk_dt = -4 * k - 5 * y
    dy_dt = k 

    return dk_dt, dy_dt

sol = odeint(diff_func, z0, t)

plt.plot(t, sol)
plt.savefig('task4')