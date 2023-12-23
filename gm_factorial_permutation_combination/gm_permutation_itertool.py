# gm_permutation_itertools: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Permutation: itertools function ***')
# ---------------------------------------------------------
import itertools as itt

# =========================================================
## --- main routine --- ##
ls = (0, 1, 2)
print(f'{list(itt.permutations(ls, 2)) = }')
print()
for i in range(1, 3):
    print(f'{i = }, {list(itt.permutations(ls, i)) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Permutation: itertools function ***
list(itt.permutations(ls, 2)) = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

i = 1, list(itt.permutations(ls, i)) = [(0,), (1,), (2,)]
i = 2, list(itt.permutations(ls, i)) = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
'''