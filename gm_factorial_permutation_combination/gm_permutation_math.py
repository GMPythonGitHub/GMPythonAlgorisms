# gm_permutation_math: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Permutation: math function ***')
# ---------------------------------------------------------
import math

# =========================================================
## --- main routine --- ##
print(f'{math.perm(6, 3) = }')
print()
for i in range(3, 7):
    print(f'{i = }, {math.perm(i, 3) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Permutation: math function ***
math.perm(6, 3) = 120

i = 3, math.perm(i, 3) = 6
i = 4, math.perm(i, 3) = 24
i = 5, math.perm(i, 3) = 60
i = 6, math.perm(i, 3) = 120
'''