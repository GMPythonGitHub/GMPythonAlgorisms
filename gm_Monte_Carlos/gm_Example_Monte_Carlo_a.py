# gm_Example_Monte_Carlo_a: coded by Kinya MIURA 230414
# -----------------------------------------------------------------------------
print('\n*** Monte Carlo Method: Circle ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import numpy as np

num, cnt = 10, 0
for i in range(num):
    xx, yy = np.random.rand(), np.random.rand()
    if np.sqrt(xx * xx + yy * yy) < 1.:
        cnt += 1
pai = 4 * cnt / num
print(f'{pai = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Monte Carlo Method: Circle ***
# -----------------------------------------------------------------------------
pai = 2.8
'''