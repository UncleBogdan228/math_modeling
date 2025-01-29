import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1 ,0.01)
x0 = -71
y0 = 1
zet0 = -3
z0 = x0, y0, zet0

def diff_func(z, t): 
    x, y, zet = z

    dx_dt = (2 * x) - y + zet
    dy_dt = x + y + zet
    dzet_dt = (4 * x) - y + (4 * zet)

    return dx_dt, dy_dt, dzet_dt

sol = odeint(diff_func, z0, t)

plt.plot(t, sol)
plt.savefig('task1_dop.png')