# gm_divisor: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Devisor: listing ***')

# =========================================================
## --- main routine --- ##
def divisors(num):
    divisors = []  # list of devisors
    for fac in range(1, num + 1):
        if num % fac == 0:
            divisors.append(fac)
    return divisors

num = 180
divs = divisors(num)
print(f'{num = }')
print(f'{divs = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Devisor: listing ***
number = 180
divisors = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 30, 36, 45, 60, 90, 180]
'''