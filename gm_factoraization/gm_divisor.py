# gm_divisor: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Devisor: listing ***')

# =========================================================
## --- main routine --- ##
number = 180
divisors = []  # list of devisors
for fac in range(1,number+1):
    if number % fac == 0:
        divisors.append(fac)
print(f'{number = }')
print(f'{divisors = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Devisor: listing ***
number = 180
divisors = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 30, 36, 45, 60, 90, 180]
'''