# gm_prime_number_list: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Prime numbers: judging numbers using list ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
number = 60
numbers = [True] * (number+1)  # table of numbers
numbers[0], numbers[1] = False, False  # '0' and '1' are not prime number
primes = []  # 'list' of prime numbers
for i, num in enumerate(numbers):
    if num:
        primes.append(i)
        ii = np.square(i)
        while ii <= number:
            numbers[ii] = False
            ii += i
print(f'{number = }')
print(f'{primes = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Prime numbers: judging numbers using list ***
number = 60
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
'''