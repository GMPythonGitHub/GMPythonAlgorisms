# gm_rc_factorial.py: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Recursive call: factorial ***')

# =========================================================
## --- defining function --- ##
def rc_factorial(nn) -> int:
    if nn == 1 or nn == 0:
        return 1
    elif nn > 1:
        return nn * rc_factorial(nn-1)
    else:
        return None

## --- main routine --- ##
print(f'{rc_factorial(5) = }')
print()
for i in range(6):
    print(f'{i = }, {rc_factorial(i) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Recursive call: factorial ***
rc_factorial(5) = 120

i = 0, rc_factorial(i) = 1
i = 1, rc_factorial(i) = 1
i = 2, rc_factorial(i) = 2
i = 3, rc_factorial(i) = 6
i = 4, rc_factorial(i) = 24
i = 5, rc_factorial(i) = 120
'''