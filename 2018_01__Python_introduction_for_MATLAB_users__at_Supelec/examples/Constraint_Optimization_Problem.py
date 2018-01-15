#! /usr/bin/env python
# -*- coding: utf8 -*-

from scipy.optimize import minimize

def obj(x):
    """Objective function to minimize."""
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

x0 = (2, 0)  # first guess
bnds = ((0, None), (0, None))  # [0, +oo) for x and y
cons = ({'type': 'ineq', 'fun': lambda x: x[0]-2*x[1]+2},
        {'type': 'ineq', 'fun': lambda x: -x[0]-2*x[1]+6},
        {'type': 'ineq', 'fun': lambda x: -x[0]+2*x[1]+2})

res = minimize(obj, x0, method='SLSQP', bounds=bnds,
               constraints=cons)

print("Minimum is", res.x)  # (1.4, 1.7)
