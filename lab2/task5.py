import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12],
], dtype=float)

# Центрирование: из каждого столбца вычитаем его среднее.
# После этого среднее по каждому признаку равно 0.
means = X.mean(axis=0)
X_centered = X - means

print('Средние по столбцам:', means)
print('Центрированная матрица:')
print(X_centered)

# Ковариационная матрица.
# n — число объектов (строк). Делим на n - 1, как в несмещённой оценке.
n = X.shape[0]
C = (1 / (n - 1)) * (X_centered.T @ X_centered)

print('Ковариационная матрица C:')
print(C)

# Собственные числа и векторы. Столбцы P — собственные векторы.
lambdas, P = np.linalg.eig(C)

# Сортируем по убыванию собственного числа.
# Вместе с числом переставляем и его вектор.
order = np.argsort(lambdas)[::-1]
lambdas = lambdas[order]
P = P[:, order]

print('Собственные числа (по убыванию):', np.round(lambdas.real, decimals=10))
print('Собственные векторы (столбцы):')
print(np.round(P.real, decimals=10))

# PCA: берём первые 2 главных компоненты и проецируем центрированные данные.
# Новые координаты объекта — это X_centered * (два первых вектора).
W = P[:, :2].real
X_pca = X_centered @ W

print('Проекция на 2 главные компоненты:')
print(np.round(X_pca, decimals=10))

# Точки на плоскости первых двух компонент.
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA: проекция на 2 главные компоненты')
plt.grid(True)
plt.show()
