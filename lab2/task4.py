import numpy as np

A = np.array([
    [4, 1, 1],
    [1, 4, 1],
    [1, 1, 4],
], dtype=float)

# eig возвращает собственные числа и матрицу P.
# Столбцы P — собственные векторы: A * v = лямбда * v.
lambdas, P = np.linalg.eig(A)

print('A =')
print(A)
print('Собственные числа:', np.round(lambdas, decimals=10))
print('Собственные векторы (столбцы P):')
print(np.round(P, decimals=10))

# Проверяем равенство для каждого столбца P.
print('Проверка A*v = лямбда*v:')
for i in range(3):
    v = P[:, i]
    left = A @ v
    right = lambdas[i] * v
    print(i + 1, np.allclose(left, right))

# В базисе из собственных векторов матрица становится диагональной:
# D = P^(-1) * A * P, на диагонали стоят собственные числа.
D = np.linalg.inv(P) @ A @ P
print('D = P^(-1)*A*P =')
print(np.round(D, decimals=10))
print('Матрица диагональная:', np.allclose(D, np.diag(lambdas)))
