import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 240, 0.01)

def bazilchiki (n, t):
    dndt = k * n
    return dndt

k = 1/15 
n_0 = 300

n_t = odeint(bazilchiki, n_0, t)

plt.plot(t, n_t[:,0], label='Размножение бактерий')
plt.xlabel('Период размножения, секунды')
plt.ylabel('Функция размножения')
plt.title('Размножение стафилококиков')
plt.legend()
plt.savefig('stafilokokiki.png')