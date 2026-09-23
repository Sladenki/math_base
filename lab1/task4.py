import numpy as np

# Система уравнений:
# x + 2y = 5
# 3x + 4y = 11

# Матрица коэффициентов
A = np.array([[1, 2],
              [3, 4]])
# Вектор правой части
B = np.array([5, 11])

# 1. Решение с помощью обратной матрицы
X_inv = np.linalg.inv(A) @ B
print("Решение через обратную матрицу:", X_inv)

# 2. Решение с помощью np.linalg.solve (более предпочтительно)
X_solve = np.linalg.solve(A, B)
print("Решение с помощью np.linalg.solve:", X_solve)

