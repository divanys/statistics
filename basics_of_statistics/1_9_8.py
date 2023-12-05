import math
from scipy import stats

# Рассчитайте 99% доверительный интервал для следующего примера:
# xˉ=10
# sd=5
# n=100

percent = 0.99
x = 10
sd = 5
n = 100


def confidence_interval(sd, X, N, percent):
    alpha = 1 - percent
    z = abs(stats.norm.ppf(alpha / 2))
    se = sd / math.sqrt(N)

    return (round(X - z * se, 2), round(X + z * se, 2))


print(confidence_interval(sd, x, n, percent))  # (8.71, 11.29)
