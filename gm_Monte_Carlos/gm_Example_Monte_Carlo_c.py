# gm_Example_Monte_Carlo_c: coded by Kinya MIURA 230414
# -----------------------------------------------------------------------------
print("\n*** Monde Carlo Method: Buffon's needle ***")
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import numpy as np

dd, ll = 1, 1
num, cnt = 10, 0
for i in range(num):
    yy, th = np.random.rand() * dd / 2, np.random.rand() * np.pi / 2
    if ll / 2 * np.sin(th) > yy:
        cnt += 1
pai = num / cnt * ll * 2 / dd
print(f'{pai = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Monde Carlo Method: Buffon's needle ***
# -----------------------------------------------------------------------------
pai = 2.5
'''