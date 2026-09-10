import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Матричное произведение A * B
A_times_B = A @ B
print("A * B:\n", A_times_B)

# Поэлементное умножение (оператор *)
A_elementwise_B = A * B
print("\nA * B (поэлементно):\n", A_elementwise_B)

# Пример с неподходящими размерами (должно вызвать ошибку)
# A = np.array([[1, 2, 3]])
# B = np.array([[4], [5]]) # Размеры 1x3 и 2x1 не согласованы
# A @ B # Ошибка: shapes (1,3) and (2,1) not aligned: 3 (dim 1) != 2 (dim 0)