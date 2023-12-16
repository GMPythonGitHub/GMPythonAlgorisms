# gm_prime_number: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Prime number: judging sequential numbers ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
number = 60
primes = []  # 'list' of prime numbers
for num in range(2, number+1):
    flg = False
    for i in range(2, int(np.sqrt(num))+1):  # from 2 until sqrt(num)+1
        if num % i == 0:
            flg = True
            break
    if not flg:
        primes.append(num)
print(f'{number = }')
print(f'{primes = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Prime number: judging sequential numbers ***
number = 60
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
'''