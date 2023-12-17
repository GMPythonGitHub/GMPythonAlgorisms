# gm_prime_factor_list: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Prime factor: listing ***')

# =========================================================
## --- main routine --- ##
number = 60 * 60 * 24
prmfac_list = []  # list of prime factors
num, prmfac = number, 2
while num > 1:
    if num % prmfac == 0:
        prmfac_list.append(prmfac)
        num //= prmfac
    else:
        prmfac += 1
print(f'{number = }')
print(f'{prmfac_list = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Prime factor: listing ***
number = 86400
prmfac_list = [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5]
'''