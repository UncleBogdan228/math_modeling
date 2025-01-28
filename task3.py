import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 30, 0.1)
a_0 = 10
v = 1
y = -0.5
m = 70


def deltav (y, t, a_0):
    dvdt = a_0 - (y/m)*v**2
    return dvdt



v_t = odeint(deltav, m, t, args=(a_0,))

plt.plot(t, v_t[:,0], label='скорость')
plt.xlabel('')
plt.ylabel('время')
plt.title('изменение скорости')
plt.legend()
plt.savefig('deltav.png')