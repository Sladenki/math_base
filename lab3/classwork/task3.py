import numpy as np
import matplotlib.pyplot as plt

def bayes(P_spam, P_w_spam, P_w_ham):
    P_ham = 1 - P_spam
    P_w = P_w_spam * P_spam + P_w_ham * P_ham
    return (P_w_spam * P_spam) / P_w

# Точечный расчёт
P_spam = 0.3
P_w_spam = 0.8
P_w_ham = 0.05
posterior = bayes(P_spam, P_w_spam, P_w_ham)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Левый график: априорная vs апостериорная ---
labels = ['Априорная', 'Апостериорная']
values = [P_spam, posterior]
colors = ['#c44e52', '#2ca02c']
bars = ax1.bar(labels, values, color=colors, edgecolor='black', width=0.6)
ax1.set_ylim(0, 1)
ax1.set_ylabel('Вероятность')
ax1.set_title('Обновление вероятности по формуле Байеса')
ax1.grid(axis='y', linestyle='-', alpha=0.3)
for bar, val in zip(bars, values):
    ax1.text(bar.get_x() + bar.get_width() / 2, val + 0.03,
             f'{val:.3f}', ha='center', fontweight='bold')

# --- Правый график: тепловая карта ---
priors = np.linspace(0.01, 0.99, 50)
likes = np.linspace(0.5, 1.0, 50)
Z = np.array([[bayes(p, l, P_w_ham) for p in priors] for l in likes])
im = ax2.imshow(Z, aspect='auto', origin='lower', cmap='RdYlBu_r',
                extent=[priors[0], priors[-1], likes[0], likes[-1]])
ax2.scatter([P_spam], [P_w_spam], color='yellow', edgecolors='black',
            s=80, zorder=5, label='Исходная конфигурация')
ax2.set_xlabel('P(спам)')
ax2.set_ylabel('P(«выигрыш» | спам)')
ax2.set_title('Апостериорная P(спам | слово)')
ax2.legend(loc='lower right')

plt.tight_layout()
plt.show()
