# gm_prime_factor: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Prime factor: list and dict ***')

# =========================================================
## --- main routine --- ##
def primefactors(num):
    prmfac_list = []  # list of prime factors
    prmfac_dict = dict([])  # dict of prime factors
    nn, prmfac = num, 2
    while nn > 1:
        if nn % prmfac == 0:
            prmfac_list.append(prmfac)
            if prmfac in prmfac_dict:
                prmfac_dict[prmfac] += 1
            else:
                prmfac_dict[prmfac] = 1
            nn //= prmfac
        else:
            prmfac += 1
    return prmfac_list, prmfac_dict

num = 60 * 60 * 24
prmfac_list, prmfac_dict = primefactors(num)
print(f'{num = }')
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

