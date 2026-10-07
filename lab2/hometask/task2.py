import numpy as np

# Оператор A в базисе e1, e2
A = np.array([
    [1, 2],
    [3, 4],
], dtype=float)

# Новый базис: f1 = e1 + e2, f2 = e1 - e2
# Столбцы T — координаты новых базисных векторов в старом базисе
T = np.array([
    [1, 1],
    [1, -1],
], dtype=float)

# Матрица оператора в новом базисе: A' = T^(-1) * A * T
A_new = np.linalg.inv(T) @ A @ T

print('A =')
print(A)
print('T (матрица перехода) =')
print(T)
print("A' = T^(-1) * A * T =")
print(np.round(A_new, decimals=10))
