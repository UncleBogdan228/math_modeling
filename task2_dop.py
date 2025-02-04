import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0.1, 5 ,0.001)
y0 = 0.1
k0 = 1
z0 = k0, y0

def diff_func(z, t): 
    k, y = z

    dk_dt = (k**2 - (3*y**2)/(t**0.5))/y
    dy_dt = k 

    return dk_dt, dy_dt

sol = odeint(diff_func, z0, t)

plt.plot(t, sol)
plt.savefig('task2_dop.png')