import numpy as np


def is_linearly_independent(vectors) -> bool:
    """Проверяет, линейно независимы ли векторы (строки матрицы)."""
    A = np.array(vectors, dtype=float)
    # Независимы, если ранг равен числу векторов
    return np.linalg.matrix_rank(A) == len(vectors)


# Пример: два неколлинеарных вектора — независимы
v1 = [[1, 0],
      [0, 1]]
print('Независимы:', is_linearly_independent(v1))

# Пример: второй вектор кратен первому — зависимы
v2 = [[1, 2, 3],
      [2, 4, 6]]
print('Независимы:', is_linearly_independent(v2))
