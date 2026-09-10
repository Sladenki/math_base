import numpy as np

# Создание матрицы 2x3
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Создание матрицы 3x2
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Матрица A:\n", A)
print("Размер матрицы A:", A.shape)
print("\nМатрица B:\n", B)
print("Размер матрицы B:", B.shape)

# Создание единичной матрицы 3x3
I = np.eye(3)
print("\nЕдиничная матрица I:\n", I)
