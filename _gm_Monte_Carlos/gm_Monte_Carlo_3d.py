# gm_Monte_Carlo_3d: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Monte Carlo Method: Sphere ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
num, cnt = 100, 0
for i in range(num):
    xx = np.random.rand() * 2. - 1.
    yy = np.random.rand() * 2. - 1.
    zz = np.random.rand() * 2. - 1.
    # spherical domain; 2 * 2 * 2
    if xx * xx + yy * yy + zz * zz < 1.:
        cnt += 1  # counting points inside sphere
pai = 8 / (4/3) * cnt / num # estimating pai
print('total number of points: ', f'{num = :d}')
print('number of points inside sphere: ', f'{cnt = :d}')
print('estimated value of pai: ', f'{pai = :g}')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Monte Carlo Method: Sphere ***
total number of points:  num = 100
number of points inside sphere:  cnt = 44
estimated value of pai:  pai = 2.64
'''