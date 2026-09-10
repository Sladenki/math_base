import numpy as np

# Определитель матрицы
M = np.array([[1, 2],
              [3, 4]])
det_M = np.linalg.det(M)
print(f"Матрица M:\n{M}")
print(f"Определитель det(M) = {det_M}") # Выведет: -2.0
