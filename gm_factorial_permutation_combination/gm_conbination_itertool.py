# gm_combination_itertools: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Combination: itertools function ***')
# ---------------------------------------------------------
import itertools as itt

# =========================================================
## --- main routine --- ##
ls = (0, 1, 2, 3)
print(f'{list(itt.combinations(ls, 2)) = }')
print()
for i in range(1, 4):
    print(f'{i = }, {list(itt.combinations(ls, i)) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Combination: itertools function ***
list(itt.combinations(ls, 2)) = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

i = 1, list(itt.combinations(ls, i)) = [(0,), (1,), (2,), (3,)]
i = 2, list(itt.combinations(ls, i)) = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
i = 3, list(itt.combinations(ls, i)) = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
'''