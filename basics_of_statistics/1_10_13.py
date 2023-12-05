from math import sqrt
import scipy.stats as st

p = 0.99
alpha = (1 - p) / 2
k_sigma = st.norm.isf(alpha)
sd = 10
se = (142 - 136) / k_sigma
print(se)  # 2.329346898776786
n = (sd / se) ** 2
print(n)  # 18.430268336170037
