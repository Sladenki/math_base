import numpy as np
from fractions import Fraction

a = np.array([2, -1, 3], dtype=float)
b = np.array([0, 2, 1], dtype=float)
c = np.array([-1, 3, 2], dtype=float)
d = np.array([1, 0, 2], dtype=float)

# Столбцы матрицы — векторы a, b, c
A = np.column_stack((a, b, c))
print('Матрица со столбцами a, b, c:')
print(A)

# Определитель
det_A = np.linalg.det(A)
print('Определитель:', det_A)

# Ранг
rank_A = np.linalg.matrix_rank(A)
print('Ранг:', rank_A)

# Базис в R^3: три вектора линейно независимы (det != 0, ранг = 3)
if rank_A == 3:
    print('Векторы a, b, c образуют базис в R^3.')

    # Координаты d: A * x = d
    coords = np.linalg.solve(A, d)
    exact = [Fraction(x).limit_denominator() for x in coords]
    print('Координаты d в базисе (a, b, c):', exact)

    # Проверка: x1*a + x2*b + x3*c = d
    check = A @ coords
    print('Проверка A * x:', np.round(check, decimals=10))
else:
    print('Векторы a, b, c не образуют базис в R^3.')
    # Ненулевое решение A * k = 0 — коэффициенты линейной зависимости
    _, _, vt = np.linalg.svd(A)
    k = vt[-1]
    exact_k = [Fraction(x).limit_denominator() for x in k]
    print('Коэффициенты линейной зависимости (k1*a + k2*b + k3*c = 0):', exact_k)
