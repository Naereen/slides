#! /usr/bin/env python
# -*- coding: utf8 -*-

import numpy as np                # standard convention
import matplotlib.pyplot as plt   # standard convention
from scipy.integrate import quad  # need only 1 function


def Ei(x, minfloat=1e-6, maxfloat=1000):
    def f(t):
        return np.exp(-t) / t
    if x > 0:
        return -1.0 * (quad(f, -x, -minfloat)[0]
                       + quad(f, minfloat, maxfloat)[0])
    else:
        return -1.0 * quad(f, -x, maxfloat)[0]


X = np.linspace(-1, 1, 1000)  # 1000 points
Y = np.vectorize(Ei)(X)       # or [Ei(x) for x in X]
plt.plot(X, Y)                # MATLAB-like interface
plt.title("The function Ei(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("figures/Ei_integral.png")
plt.show()
