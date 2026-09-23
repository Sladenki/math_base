import numpy as np

# Матрицы A (2×3) и B (3×2)
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Матричное произведение C = A · B
C = A @ B
print('C = A · B:')
print(C)

# Транспонирование C
C_T = C.T
print('Транспонированная матрица C:')
print(C_T)

# Определитель матрицы D
D = np.array([[4, 7],
              [2, 6]])
det_D = np.linalg.det(D)
print('Определитель D:', det_D)

# Обратная матрица и проверка D · D⁻¹ = I
D_inv = np.linalg.inv(D)
print('Обратная матрица D:')
print(D_inv)

I = D @ D_inv
print('D * D^(-1):')
print(np.round(I, decimals=10))  # округляем, чтобы убрать погрешность float
