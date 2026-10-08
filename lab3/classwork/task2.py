import numpy as np
import matplotlib.pyplot as plt

def theoretical_p(n, days=365): 
    p_no = 1.0
    for i in range(n):
        p_no *= (days - i) / days
    return 1 - p_no

def empirical_p(n, trials=1000, days=365): 
    hits = 0
    for _ in range(trials):
        bdays = np.random.randint(0, days, size=n) 
        if len(set(bdays)) < n:
            hits += 1
    p = hits / trials
    sigma = np.sqrt(p * (1 - p) / trials) 
    return p, sigma

ns= np.arange(2, 61)
theo = [theoretical_p(n) for n in ns]
emp, err = zip(*[empirical_p(n) for n in ns])

plt.plot(ns, theo, 'r-', label='Теоретическая P(n)')
plt.errorbar(ns, emp, yerr=[2 * e for e in err],
             fmt='o', label='эмпирическая ± 2σ')
plt.legend()
plt.show()