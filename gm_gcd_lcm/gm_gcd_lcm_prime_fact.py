# gm_gcd_lcm_prime_fact: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Greatest common divisor and Least common multiple ***')

# =========================================================
## --- defining function for plime factor list --- ##
def prmfac_list(number) -> list:
    prmfac_list = []  # list of prime factors
    num, prmfac = number, 2
    while num > 1:
        if num % prmfac == 0:
            prmfac_list.append(prmfac)
            num //= prmfac
        else:
            prmfac += 1
    return prmfac_list
def prmfac_dict(number) -> dict:
    prmfac_dict = {}  # dict of prime factors
    num, prmfac = number, 2
    while num > 1:
        if num % prmfac == 0:
            if prmfac not in prmfac_dict:
                prmfac_dict[prmfac] = 1
            else:
                prmfac_dict[prmfac] += 1
            num //= prmfac
        else:
            prmfac += 1
    return prmfac_dict

# =========================================================
## --- main routine --- ##
numbers = [36, 120, 100]
prmfac_lists = [prmfac_list(num) for num in numbers]
prmfac_dicts = [prmfac_dict(num) for num in numbers]
print(f'{numbers = }')
print(f'{prmfac_lists = }')
print(f'{prmfac_dicts = }')

prmfac_set = set()
for prmfac_list in prmfac_lists:
    # prmfac_set = prmfac_set.union(prmfac_list)
    prmfac_set |= set(prmfac_list)
print(prmfac_set)

gcd_dict, lcm_dict = {}, {}
gcd = lcm = 1
for prmfac in prmfac_set:
    prmfacs = []
    for prmfac_dict in prmfac_dicts:
        if prmfac in prmfac_dict:
            prmfacs.append(prmfac_dict[prmfac])
        else:
            prmfacs.append(0)
    gcd_dict[prmfac] = min(prmfacs)
    gcd *= prmfac**min(prmfacs)
    lcm_dict[prmfac] = max(prmfacs)
    lcm *= prmfac**max(prmfacs)
print(f'{gcd_dict = }')
print(f'{gcd = }')
print(f'{lcm_dict = }')
print(f'{lcm = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Greatest common divisor and Least common multiple ***
numbers = [36, 120, 100]
prmfac_lists = [[2, 2, 3, 3], [2, 2, 2, 3, 5], [2, 2, 5, 5]]
prmfac_dicts = [{2: 2, 3: 2}, {2: 3, 3: 1, 5: 1}, {2: 2, 5: 2}]
{2, 3, 5}
gcd_dict = {2: 2, 3: 0, 5: 0}
gcd = 4
lcm_dict = {2: 3, 3: 2, 5: 2}
lcm = 1800
'''