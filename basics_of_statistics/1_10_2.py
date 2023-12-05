from math import sqrt
import scipy.stats as st

sp = 20
n = 64
mean = 18.5
std = 4

se = std / sqrt(n)
z_value = (mean - sp) / se
p_score = st.norm.cdf(z_value) * 2
print(p_score)  # проверка нулевой гипотезы методом p-уровня значимости
# если p < 0.05, то H[0] ошибочна
# но на самом деле сама проверка данным образом хуета (можно подставить значения и подстроить результат)
