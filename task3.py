import numpy as np

# Создаём матрицу
A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Определитель
det_A = np.linalg.det(A)
print('Определитель матрицы A:', det_A)

# Ранг
rank_A = np.linalg.matrix_rank(A)
print('Ранг матрицы A:', rank_A)

check_row = 2 * A[1] - A[0]
print(f'Проверка: 2*R2 - R1 = {check_row}. Совпадает с R3? {np.array_equal(check_row, A[2])}')