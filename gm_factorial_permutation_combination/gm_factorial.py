# gm_factorial: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Factorial: definition ***')

# =========================================================
## --- defining function --- ##
def factorial(n) -> int:
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

## --- main routine --- ##
print(f'{factorial(5) = }')
print()
for i in range(6):
    print(f'{i = }, {factorial(i) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Factorial: definition ***
factorial(5) = 120

i = 0, factorial(i) = 1
i = 1, factorial(i) = 1
i = 2, factorial(i) = 2
i = 3, factorial(i) = 6
i = 4, factorial(i) = 24
i = 5, factorial(i) = 120
'''