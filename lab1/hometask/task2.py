import numpy as np
import sympy as sp

# Система:
# 2x − 3y + z = 1
#  x +  y + z = 5
# 3x − 2y − z = 0

# --- NumPy ---
A = np.array([[2, -3, 1],
              [1,  1, 1],
              [3, -2, -1]], dtype=float)
B = np.array([1, 5, 0], dtype=float)

# Решение СЛАУ
X = np.linalg.solve(A, B)
print('Решение NumPy (x, y, z):', X)

# --- SymPy ---
x, y, z = sp.symbols('x y z')

# Та же система в символьном виде
eqs = [
    sp.Eq(2*x - 3*y + z, 1),
    sp.Eq(x + y + z, 5),
    sp.Eq(3*x - 2*y - z, 0),
]

# linsolve решает систему линейных уравнений
solution = sp.linsolve(eqs, [x, y, z])
print('Решение SymPy:', solution)
