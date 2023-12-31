from scipy import stats

# Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение со средним значением
# равным 100 и стандартным отклонением равным 15 (M = 100, sd = 15).
# Какой приблизительно процент людей обладает IQ  на промежутке от 70 до 112
mean = 100  # среднее
std = 15  # sd
IQ1 = 70  # выбранный x1[i]
IQ2 = 112
z1 = (70 - 100) / 15
z2 = (112 - 100) / 15
print(f'На промежутке [-2σ ; 0,8σ] расположено {abs((stats.norm.cdf(z1) - stats.norm.cdf(z2))):.2%} значений')  # 76.54%
