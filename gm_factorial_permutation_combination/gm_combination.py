# gm_permutation: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Combination: definition ***')

# =========================================================
## --- defining function --- ##
def permutation(n, m) -> int:
    num = 1
    for i in range(n-m+1, n+1):
        num *= i
    return num
def combination(n, m) -> int:
    return permutation(n,m) // permutation(m,m)

## --- main routine --- ##
print(f'{combination(6, 3) = }')
print()
for i in range(3, 7):
    print(f'{i = }, {combination(i, 3) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** combination: definition ***
combination(6, 3) = 20

i = 3, combination(i, 3) = 1
i = 4, combination(i, 3) = 4
i = 5, combination(i, 3) = 10
i = 6, combination(i, 3) = 20
'''