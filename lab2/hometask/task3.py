import numpy as np
import matplotlib.pyplot as plt

# Симметричная матрица — собственные векторы ортогональны
M = np.array([
    [4, 1],
    [1, 4],
], dtype=float)

# --- вручную (проверка) ---
# det(M - lam*I) = (4-lam)^2 - 1 = 0  =>  4-lam = +/-1  =>  lam1 = 5, lam2 = 3
# lam=5: (M-5I)v=0 => -x+y=0  => v1 = (1, 1)
# lam=3: (M-3I)v=0 =>  x+y=0  => v2 = (1,-1)
# v1 · v2 = 1 - 1 = 0 — ортогональны

print('Вручную: lambda = 5, 3;  v1 = (1, 1), v2 = (1, -1)')

# --- NumPy ---
lambdas, P = np.linalg.eig(M)
print('NumPy собственные числа:', np.round(lambdas, decimals=10))
print('NumPy собственные векторы (столбцы):')
print(np.round(P, decimals=10))

v1, v2 = P[:, 0], P[:, 1]
print('Ортогональность v1·v2 =', np.round(np.dot(v1, v2), decimals=12))
print('Проверка M*v = lam*v:')
for i in range(2):
    print(i + 1, np.allclose(M @ P[:, i], lambdas[i] * P[:, i]))

# Преобразование единичного круга: точки (cos t, sin t) умножаем на M
t = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack((np.cos(t), np.sin(t)))
ellipse = M @ circle

plt.figure(figsize=(6, 6))
plt.plot(circle[0], circle[1], label='единичный круг')
plt.plot(ellipse[0], ellipse[1], label='образ M·круг')

# Направления собственных векторов (оси эллипса)
scale = np.abs(lambdas)
for i, color in enumerate(['C2', 'C3']):
    v = P[:, i]
    v = v / np.linalg.norm(v)
    plt.arrow(0, 0, scale[i] * v[0], scale[i] * v[1],
              head_width=0.15, length_includes_head=True, color=color,
              label=f'lam={lambdas[i]:.0f}, v')

plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title('Преобразование единичного круга матрицей M')
plt.show()
