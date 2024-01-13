# gm_rc_summation.py: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** FRecursive call: summation ***')

# =========================================================
## --- defining function --- ##
def rc_summation(nn) -> int:
    if nn == 0:
        return 0
    elif nn > 0:
        return nn + rc_summation(nn-1)
    else:
        return None

## --- main routine --- ##
print(f'{rc_summation(5) = }')
print()
for i in range(6):
    print(f'{i = }, {rc_summation(i) = }')
# =============================================================
# terminal log / terminal log / terminal log /
'''
*** FRecursive call: summation ***
rc_summation(5) = 15

i = 0, rc_summation(i) = 0
i = 1, rc_summation(i) = 1
i = 2, rc_summation(i) = 3
i = 3, rc_summation(i) = 6
i = 4, rc_summation(i) = 10
i = 5, rc_summation(i) = 15
'''