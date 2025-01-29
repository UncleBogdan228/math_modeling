import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#определяем переменную
t = np.arange(0,10,0.01)

#определяем фунцкию
def diff_func(z, t): # z - изменяемая величична для системы
    theta, omega = z #указание изменяемых функций через z

    #первое и второе уравнение системы
    dtheta_dt = omega
    domega_dt = -k * omega - c * np.sin(theta) 

    return dtheta_dt, domega_dt

# начальные значения и параметры входящие в систему
theta0 = np.pi - 0.1
omega0 = 0
#начальное значение изменяемой величины
z0 = theta0, omega0

k = 0.25
c = 5

sol = odeint(diff_func,z0, t)

plt.plot(t, sol[:, 0])
plt.savefig('theta(t)')

# альтернатива
plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')

plt.legend()
plt.savefig('fig_1.png')