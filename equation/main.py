import sympy
from sympy import symbols
from sympy.solvers import solve


x = symbols('x')

eq = x**2 - 2

print('x = ',solve(eq,x))