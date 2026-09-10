import numpy as np

# Обратная матрица

A = np.array([[2, 3],
              [1, 4]])
det_A = np.linalg.det(A)
print(f"det(A) = {det_A}")

A_inv = np.linalg.inv(A)
print("Обратная матрица A^{-1}:\n", A_inv)

# Проверка: A * A^{-1} = I
identity = A @ A_inv
# Округлим для красивого вывода
print("\nA * A^{-1}:\n", np.round(identity, decimals=5))
