import matplotlib.pyplot as plt
from math import sqrt

p = 0.25
z = 1.96
n = range(1, 501)  # Используем range для создания списка значений от 1 до 2000


def standard_deviation(p, n):
    return sqrt((p * (1 - p)) / n)


def binomial_confidence_interval(p, z, n):
    plus = []
    minus = []
    sd = []
    ps = []


    for i in n:
        sd_value = standard_deviation(p, i)
        plus.append(p + z * sd_value)
        minus.append(p - z * sd_value)
        sd.append(sd_value)

        ps.append(p)

    return plus, minus, sd, ps


plus, minus, sd, ps = binomial_confidence_interval(p, z, n)

fig, ax = plt.subplots()
ax.plot(n, plus, label='Upper Bound')
ax.plot(n, minus, label='Lower Bound')
ax.plot(n, sd, label='Standart Deviation')

ax.plot(n, ps, linestyle='--', linewidth=1, label='p')


ax.text(0.05, 0.95, f'z = {z}', transform=ax.transAxes, fontsize=12, verticalalignment='top')
ax.text(0.05, 0.90, f'p = {p}', transform=ax.transAxes, fontsize=12, verticalalignment='top')

ax.set(xlabel='Sample Size', ylabel='VPIP values',
       title='Binomial Confidence Interval')
ax.grid()
ax.legend()

plt.show()
