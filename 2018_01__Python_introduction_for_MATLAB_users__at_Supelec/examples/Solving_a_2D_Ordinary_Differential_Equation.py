#! /usr/bin/env python
# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # use Runge-Kutta 4


def pend(y, t, b, c):  # function definition
    """Gives 2D vector dy/dt as function of y and t, with parameters b and c."""
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])


b, c = 0.25, 5.0  # tuple assignment
y0 = np.array([np.pi - 0.1, 0.0])
t = np.linspace(0, 10, 101)  # on [0,10] with 101 points

sol = odeint(pend, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')  # blue
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')  # green
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("figures/Pendulum_solution.png")
plt.show()
