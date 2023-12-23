# gm_combination_math: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Combination: math function ***')
# ---------------------------------------------------------
import math

# =========================================================
## --- main routine --- ##
print(f'{math.comb(6, 3) = }')
print()
for i in range(3, 7):
    print(f'{i = }, {math.comb(i, 3) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Combination: math function ***
math.comb(6, 3) = 20

i = 3, math.comb(i, 3) = 1
i = 4, math.comb(i, 3) = 4
i = 5, math.comb(i, 3) = 10
i = 6, math.comb(i, 3) = 20
'''