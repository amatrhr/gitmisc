from sympy import *
x, t, z, y, nu = symbols('x t z y nu')
init_printing()
integrate(sin(x**2), (x, -oo, oo))

expr_2 = nu*t
expr_2.subs(((nu, 100+I), (t, 11+4*I)))

