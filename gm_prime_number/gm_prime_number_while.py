# gm_prime_number_while: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Prime number: judging sequential numbers with while loop ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
number = 60
primes = []  # 'list' of prime numbers
for num in range(2, number+1):
    i, flg = 0, False
    while i < len(primes) and primes[i] <= int(np.sqrt(num))+1:  # prime numbers
        if num % primes[i] == 0:
            flg = True
            break
        i += 1
    if not flg:
        primes.append(num)
print(f'{number = }')
print(f'{primes = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Prime number: judging sequential numbers with while loop ***
number = 60
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
'''