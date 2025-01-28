import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

def bazilchiki (I, t):
    dIdt = -k * I * t
    return dIdt

k = 0.08
I_0 = 1000

I_t = odeint(bazilchiki, I_0, t)

plt.plot(t, I_t[:,0], label='потеря денег')

plt.ylabel('дни')
plt.title('мама я инвестор')
plt.legend()
plt.savefig('invest.png')