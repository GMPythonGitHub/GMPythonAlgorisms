# gm_Monte_Carlo_sine: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('***  Monte Carlo Method: sine curve ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
num, cnt = 1000, 0
for i in range(num):
    xx, yy = np.random.rand() * np.pi, np.random.rand()
    # rectangular domain; pi * 1
    if np.sin(xx) > yy:  # counting points under sine curve
        cnt += 1
area = np.pi * cnt / num  # estimating area under sine curve
print('total number of points: ', f'{num = :d}')
print('number of points under sine curve: ', f'{cnt = :d}')
print('estimated value of area: ', f'{area = :g}')

# =========================================================
# terminal log / terminal log / terminal log /
'''
***  Monte Carlo Method: sine curve ***
total number of points:  num = 1000
number of points under sine curve:  cnt = 634
estimated value of area:  area = 1.99177
'''