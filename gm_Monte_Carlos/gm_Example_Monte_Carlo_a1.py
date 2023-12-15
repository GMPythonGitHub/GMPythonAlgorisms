# gm_Example_Monte_Carlo_a1: coded by Kinya MIURA 230414
# -----------------------------------------------------------------------------
print('\n*** Monte Carlo Method: Sphere ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import numpy as np

num, cnt = 1000, 0
for i in range(num):
    xx, yy, zz = np.random.rand(), np.random.rand(), np.random.rand()
    if xx * xx + yy * yy + zz * zz < 1.:
        cnt += 1
pai = 6 * cnt / num
print(f'{pai = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Monte Carlo Method: Sphere ***
# -----------------------------------------------------------------------------
pai = 2.82
'''