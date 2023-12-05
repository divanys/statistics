from math import sqrt
import scipy.stats as st

percent = 0.95
sp = 20
n = 64
mean = 18.5
sd = 4


def confidence_interval(sd, X, N, percent):
    alpha = 1 - percent
    z = abs(st.norm.ppf(alpha / 2))  # z-значение (стд отклонение)
    se = sd / sqrt(N)  # стандартная ошибка среднего

    return (round(X - z * se, 2), round(X + z * se, 2))  # интервал при помощи формулы (x_mean + z * se)


print(confidence_interval(sd, mean, n, percent))  # (17.52, 19.48)
# 20 не принадлежит доверительному интервалу — отклоняем Н0, где p < 0.05 == 0.003
