# gm_prime_factor_count: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Prime factor: counting ***')

from collections import defaultdict

# =========================================================
## --- main routine --- ##
number = 60 * 60 * 24
prmfac_list = []  # list of prime factors
prmfac_dict = defaultdict(int)  # defaultdict of prime factors
num, prmfac = number, 2
while num > 1:
    if num % prmfac == 0:
        prmfac_list.append(prmfac)
        prmfac_dict[prmfac] += 1
        num //= prmfac
    else:
        prmfac += 1
print(f'{number = }')
print(f'{prmfac_list = }')
print(f'{prmfac_dict = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Factor: counting ***
number = 86400
prmfac_list = [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5]
prmfac_dict = {2: 7, 3: 3, 5: 2}
'''

