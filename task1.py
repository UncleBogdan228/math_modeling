import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5 ,0.01)
y0 = 1
zet0 = -3
z0 = zet0, y0

def diff_func(z, x): 
    zet, y = z

    dzet_dx = zet/x - y * zet ** 2
    dy_dx = y**2 * zet

    return dzet_dx, dy_dx

sol = odeint(diff_func, z0, x)

plt.plot(x, sol)
plt.savefig('task1')

