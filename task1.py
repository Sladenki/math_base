import numpy as np

# Создаём матрицу
A = np.array([[4, 7],
              [2, 6]])

# Определитель
det_A = np.linalg.det(A)
print('Определитель матрицы A:', det_A)

# Ранг
rank_A = np.linalg.matrix_rank(A)
print('Ранг матрицы A:', rank_A)


# Обратная матрица
A_inv = np.linalg.inv(A)
print('Обратная матрица A:', A_inv)


