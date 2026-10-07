import numpy as np
from itertools import combinations

# В R^3 даны четыре вектора (a2 = 2*a1, поэтому зависимы)
a1 = np.array([1, 2, 3], dtype=float)
a2 = np.array([2, 4, 6], dtype=float)
a3 = np.array([3, 1, 1], dtype=float)
a4 = np.array([1, 1, 1], dtype=float)
x = np.array([5, 7, 10], dtype=float)

vectors = {'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4}

print('Векторы:')
for name, v in vectors.items():
    print(f'  {name} =', v)
print('x =', x)

# Базис в R^3 — любые 3 линейно независимых вектора (ранг матрицы = 3)
print('\nПроверка троек (np.linalg.matrix_rank):')
bases = []
for names in combinations(vectors.keys(), 3):
    cols = np.column_stack([vectors[n] for n in names])
    rank = np.linalg.matrix_rank(cols)
    ok = rank == 3
    print(f'  {names}: ранг = {rank}', '— базис' if ok else '— не базис')
    if ok:
        bases.append(names)

# Координаты x в первом найденном базисе: A * c = x
if bases:
    names = bases[0]
    A = np.column_stack([vectors[n] for n in names])
    coords = np.linalg.solve(A, x)
    print(f'\nБазис: {names}')
    print('Матрица A (столбцы — векторы базиса):')
    print(A)
    print('Координаты x (решение A c = x):', np.round(coords, decimals=10))
    print('Проверка A @ c:', np.round(A @ coords, decimals=10))
else:
    print('\nНи одна тройка не образует базис в R^3.')
