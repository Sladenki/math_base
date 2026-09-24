import numpy as np

A = np.array([
    [2, -1, 0],
    [1, 3, 2],
    [0, 1, -2],
], dtype=float)

x = np.array([1, 2, -1], dtype=float)

# Образ вектора: A(x) = A * x
print('A =')
print(A)
print('x =', x)
print('A * x =', A @ x)

# Линейность: A(альфа*u + бета*v) = альфа*A(u) + бета*A(v)
u = np.array([1, 0, -1], dtype=float)
v = np.array([0, 1, 2], dtype=float)
alpha = 3
beta = -2

left = A @ (alpha * u + beta * v)
right = alpha * (A @ u) + beta * (A @ v)
print('Линейность выполняется:', np.allclose(left, right))

# Ядро: A * x = 0. Если det != 0, решение только нулевое.
print('det A =', np.round(np.linalg.det(A), decimals=10))
print('Ранг A:', np.linalg.matrix_rank(A))
print('Ядро: {0}')

# Образ — линейная оболочка столбцов. Ранг 3, поэтому образ = R^3.
print('Столбцы A (базис образа):')
print(A)
print('Размерность образа:', np.linalg.matrix_rank(A))
