import numpy as np

# Система уравнений:
# 2x + 3y = 8
#  x + 4y = 9

# Матрица коэффициентов
A = np.array([[2, 3],
              [1, 4]])
# Вектор правой части
B = np.array([8, 9])

# 1. Решение с помощью обратной матрицы
X_inv = np.linalg.inv(A) @ B
print("Решение через обратную матрицу:", X_inv)

# 2. Решение с помощью np.linalg.solve (более предпочтительно)
X_solve = np.linalg.solve(A, B)
print("Решение с помощью np.linalg.solve:", X_solve)
# x = 1, y = 2, т.к. 2*1 + 3*2 = 8 и 1 + 4*2 = 9