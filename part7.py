import numpy as np

# Матрица с рангом 2
A = np.array([[1, 2],
              [3, 4]])
rank_A = np.linalg.matrix_rank(A)
print(f"Ранг матрицы A: {rank_A}")

# Матрица с линейно зависимыми строками (ранг 1)
B = np.array([[1, 2],
              [2, 4]])
rank_B = np.linalg.matrix_rank(B)
print(f"Ранг матрицы B: {rank_B}")

# Матрица 3x3 с рангом 2 (одна строка - линейная комбинация других)
C = np.array([[1, 2, 3],
              [2, 4, 6],
              [0, 1, 2]])
rank_C = np.linalg.matrix_rank(C)
print(f"Ранг матрицы C: {rank_C}")
