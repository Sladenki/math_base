import numpy as np

# По условию
x = np.array([3, -4, 0, 5], dtype=float)
y = np.array([-1, 2, 3, -2], dtype=float)


# L1: складываем модули всех координат.
# Модуль нужен, потому что длина не бывает отрицательной: |-4| = 4.
# ||v||_1 = |v1| + |v2| + ... + |vn|
def norm_l1(v):
    return np.sum(np.abs(v))

# L2 (евклидова): обычная длина отрезка в пространстве.
# Сначала квадраты координат, потом сумма, потом корень.
# ||v||_2 = sqrt(v1^2 + v2^2 + ... + vn^2)
def norm_l2(v):
    return np.sqrt(np.sum(v ** 2))

# L∞ («бесконечность»): берём самую большую по модулю координату.
# Остальные координаты на результат не влияют.
# ||v||_∞ = max(|v1|, |v2|, ..., |vn|)
def norm_linf(v):
    return np.max(np.abs(v))


print('x =', x)
print('||x||_1  =', norm_l1(x))
print('||x||_2  =', norm_l2(x))
print('||x||_inf =', norm_linf(x))

print('y =', y)
print('||y||_1  =', norm_l1(y))
print('||y||_2  =', norm_l2(y))
print('||y||_inf =', norm_linf(y))

# Расстояние между двумя векторами — это норма их разности.
# Сначала вычитаем координаты, потом считаем длину получившегося вектора.
diff = x - y
print('x - y =', diff)
print('Расстояние ||x - y||:')
print('L1  =', norm_l1(diff))
print('L2  =', norm_l2(diff))
print('Linf =', norm_linf(diff))

# Неравенство треугольника
# Смысл: длина x+y не больше, чем длины x и y по отдельности, сложенные вместе.
# ||x + y|| <= ||x|| + ||y||
total = x + y
print('x + y =', total)
print('Неравенство треугольника ||x + y|| <= ||x|| + ||y||:')
for name, norm in (('L1', norm_l1), ('L2', norm_l2), ('Linf', norm_linf)):
    left = norm(total)          # ||x + y||
    right = norm(x) + norm(y)   # ||x|| + ||y||
    # 1e-12 — допуск на погрешность float при сравнении
    print(f'{name}: {left} <= {right} -> {left <= right + 1e-12}')
