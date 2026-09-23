import numpy as np

# Создаём матрицу
A = np.array([[4, 7],
              [2, 6]])

# Находим обратную матрицу
A_inv = np.linalg.inv(A)

# Перемножаем исходную и обратную матрицы
product = A @ A_inv  

# Проверяем равенство единичной матрице
is_identity = np.allclose(product, np.eye(2))

print("A * A^(-1):\n", product)
print("Равно I:", is_identity)