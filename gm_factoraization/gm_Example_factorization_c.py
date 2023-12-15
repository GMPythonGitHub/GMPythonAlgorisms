# gm_Example_factorization_c: coded by Kinya MIURA 230414
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def prime_factorization(number):
    prime_factors = []  # 'list' of prime factors
    prime_factors_dic = {}  # 'dict' of prime factors
    num, pfac = number, 2
    while num > 1:
        if num % pfac == 0:
            prime_factors.append(pfac)
            if pfac not in prime_factors_dic:
                prime_factors_dic[pfac] = 1
            else:
                prime_factors_dic[pfac] += 1
            num //= pfac
        else:
            pfac += 1
    return prime_factors, prime_factors_dic

# ////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    number = 360
    prime_factors, prime_factors_set = prime_factorization(number)
    print(f'{number = }')
    print(f'{prime_factors = }')
    print(f'{prime_factors_set = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
number = 360
prime_factors = [2, 2, 2, 3, 3, 5]
prime_factors_set = {2: 3, 3: 2, 5: 1}
'''

