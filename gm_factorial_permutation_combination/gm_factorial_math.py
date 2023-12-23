# gm_factorial: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Factorial: math function ***')
# ---------------------------------------------------------
import math

# =========================================================
## --- main routine --- ##
print(f'{math.factorial(5) = }')
print()
for i in range(6):
    print(f'{i = }, {math.factorial(i) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Factorial: using muth function ***
math.factorial(5) = 120

i = 0, math.factorial(i) = 1
i = 1, math.factorial(i) = 1
i = 2, math.factorial(i) = 2
i = 3, math.factorial(i) = 6
i = 4, math.factorial(i) = 24
i = 5, math.factorial(i) = 120
'''