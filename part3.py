import numpy as np

# Создадим две матрицы 2x2
C = np.array([[1, 2],
              [3, 4]])
D = np.array([[5, 6],
              [7, 8]])

# Сложение
C_plus_D = C + D
print("C + D:\n", C_plus_D)

# Вычитание
C_minus_D = C - D
print("\nC - D:\n", C_minus_D)

# Умножение на число
two_C = 2 * C
print("\n2 * C:\n", two_C)
