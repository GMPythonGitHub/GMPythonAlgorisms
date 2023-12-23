# gm_permutation_itertools: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Permutation: scipy.special function ***')
# ---------------------------------------------------------
import scipy.special as spsp

# =========================================================
## --- main routine --- ##
print(f'{int(spsp.perm(6, 3)) = }')
print()
for i in range(3, 7):
    print(f'{i = }, {int(spsp.perm(i, 3)) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Permutation: scipy.special function ***
int(spsp.perm(6, 3)) = 120

i = 3, int(spsp.perm(i, 3)) = 6
i = 4, int(spsp.perm(i, 3)) = 24
i = 5, int(spsp.perm(i, 3)) = 60
i = 6, int(spsp.perm(i, 3)) = 120
'''