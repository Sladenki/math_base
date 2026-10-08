# Орёл и решка

import numpy as np


def coin_toss_experiment(n_trials):
    """Моделирует n_trials подбрасываний монеты.
    Возвращает количество орлов и частоту."""
    # 0 - решка, 1 - орёл
    results = np.random.choice([0, 1], size=n_trials)
    print(results)
    heads = np.sum(results)
    print(heads)
    frequency = heads / n_trials
    return heads, frequency
# Проводим эксперименты
trials = [10]
print("Количество испытаний | Орлов | Частота | Отклонение от 0.5")
print("-" * 70)
for n in trials:
    heads, freq = coin_toss_experiment(n)
    deviation = abs(freq - 0.5)
    print(f"{n:>20} | {heads:>6} | {freq:.4f} | {deviation:.4f}")