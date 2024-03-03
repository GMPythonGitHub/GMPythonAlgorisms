# gm_Example_Monte_Carlo_a: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('\n*** Monte Carlo Method: Circle ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
num, cnt = 100, 0
for i in range(num):
    xx = np.random.rand() * 2. - 1.
    yy = np.random.rand() * 2. - 1.
    # square area; 2 * 2
    if np.sqrt(xx * xx + yy * yy) < 1.:
        cnt += 1  # counting points inside circle
pai = 4 * cnt / num  # estimating pai
print('total number of points: ', f'{num = :d}')
print('number of points inside circle: ', f'{cnt = :d}')
print('estimated value of pai: ', f'{pai = :g}')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Monte Carlo Method: Circle ***
total number of points:  num = 100
number of points inside circle:  cnt = 73
estimated value of pai:  pai = 2.92
'''