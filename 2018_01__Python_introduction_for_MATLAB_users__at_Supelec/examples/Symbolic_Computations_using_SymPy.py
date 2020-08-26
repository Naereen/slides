#! /usr/bin/env python
# -*- coding: utf8 -*-

from sympy import *
x, t, z, nu = symbols('x t z nu')

init_printing(use_unicode=True)

print(diff(sin(x)*exp(x), x))

print(integrate(exp(x)*sin(x) + exp(x)*cos(x), x))

print(integrate(sin(x**2), (x, -oo, oo)))

print(limit(sin(x)/x, x, 0))

y = Function('y')
print(dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t)))

# etc, see http://docs.sympy.org for more examples
