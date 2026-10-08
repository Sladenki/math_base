
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
p = 0.7
N = 5000

results = np.random.choice([0, 1], size=N, p=[1-p, p]) 
cum_heads = np.cumsum(results)
k = np.arange(1, N + 1)
cum_freq = cum_heads / k

# График 1: сходимость
plt.figure()
plt.plot(k, cum_freq, color='steelblue')
plt.axhline(y=p, color='red', linestyle='--')

# График 2: отклонение в лог-масштабе
deviation = np.abs(cum_freq - p)
plt.figure()
plt.semilogx(k, deviation, color='darkorange')
plt.axhline(y=0.01, color='green', linestyle=':')

plt.show()