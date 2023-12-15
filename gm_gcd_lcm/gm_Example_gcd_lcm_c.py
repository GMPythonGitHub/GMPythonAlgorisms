# gm_Example_greatest_common_divisor_c: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** ------------ ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
from gm_Example_factorization_c import prime_factorization

# -----------------------------------------------------------------------------
numbers = [36, 120, 100]

pfcts = [prime_factorization(num)[0] for num in numbers]
pfcts_dic = [prime_factorization(num)[1] for num in numbers]
print(f'{pfcts = }')
print(f'{pfcts_dic = }')

pfcts_set = set()
prime_factors_set = pfcts_set.union(*pfcts)
print(f'{prime_factors_set = }')

greatest_common_divisor_dic, least_common_multiple_dic = {}, {}
greatest_common_divisor, least_common_multiple = 1, 1
for pfct in prime_factors_set:
    dum = []
    for pfdic in pfcts_dic:
        if pfct in pfdic:
            dum.append(pfdic[pfct])
        else:
            dum.append(0)
    greatest_common_divisor_dic[pfct] = min(dum)
    greatest_common_divisor *= pfct**min(dum)
    least_common_multiple_dic[pfct] = max(dum)
    least_common_multiple *= pfct**max(dum)

print('# ------------')
print(f'{greatest_common_divisor_dic = }')
print(f'{greatest_common_divisor = }')
print('# ------------')
print(f'{least_common_multiple_dic = }')
print(f'{least_common_multiple = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
pfcts = [[2, 2, 3, 3], [2, 2, 2, 3, 5]]
pfcts_dic = [{2: 2, 3: 2}, {2: 3, 3: 1, 5: 1}]
prime_factors_set = {2, 3, 5}
# ------------
greatest_common_divisor_dic = {2: 2, 3: 1, 5: 0}
greatest_common_divisor = 12
# ------------
least_common_multiple_dic = {2: 3, 3: 2, 5: 1}
least_common_multiple = 360
'''