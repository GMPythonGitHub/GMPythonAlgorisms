# gm_permutation: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Permutation: definition ***')

# =========================================================
## --- defining function --- ##
def permutation(n, m) -> int:
    num = 1
    for i in range(n-m+1, n+1):
        num *= i
    return num

## --- main routine --- ##
print(f'{permutation(6, 3) = }')
print()
for i in range(3, 7):
    print(f'{i = }, {permutation(i, 3) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Permutation: definition ***
permutation(6, 3) = 120

i = 3, permutation(i, 3) = 6
i = 4, permutation(i, 3) = 24
i = 5, permutation(i, 3) = 60
i = 6, permutation(i, 3) = 120
'''