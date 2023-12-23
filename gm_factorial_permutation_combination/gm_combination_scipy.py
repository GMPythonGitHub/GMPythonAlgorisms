# gm_combination_itertools: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Combination: scipy.special function ***')
# ---------------------------------------------------------
import scipy.special as spsp

# =========================================================
## --- main routine --- ##
print(f'{int(spsp.comb(6, 3)) = }')
print()
for i in range(3, 7):
    print(f'{i = }, {int(spsp.comb(i, 3)) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Combination: scipy.special function ***
int(spsp.comb(6, 3)) = 20

i = 3, int(spsp.comb(i, 3)) = 1
i = 4, int(spsp.comb(i, 3)) = 4
i = 5, int(spsp.comb(i, 3)) = 10
i = 6, int(spsp.comb(i, 3)) = 20
'''