# gm_Example_Monte_Carlo_b: coded by Kinya MIURA 230414
# -----------------------------------------------------------------------------
print('\n***  Monte Carlo Method: Sine Curve ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import numpy as np

num, cnt = 10, 0
for i in range(num):
    xx, yy = np.random.rand() * np.pi / 2, np.random.rand()
    if np.sin(xx) > yy:
        cnt += 1
area = np.pi / 2 * cnt / num
print(f'{area = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Monte Carlo Method: Sine Curve ***
# -----------------------------------------------------------------------------
area = 0.47123889803846897
'''