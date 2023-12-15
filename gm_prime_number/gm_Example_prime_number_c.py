# gm_Example_prime_number_c: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def prime_numbers(number):
    numbers = list(range(number+1))  # table of numbers
    numbers[0], numbers[1] = None, None  # '0' and '1' both are not prime number
    primes = []  # 'list' of prime numbers
    for num in numbers:
        if num is not None:
            primes.append(num)
            numnum = num * num
            while numnum <= number:
                numbers[numnum] = None
                numnum += num
    return primes

# ////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    number = 60
    print(f'{number = }')
    print(f'{prime_numbers(number) = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
number = 60
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
'''