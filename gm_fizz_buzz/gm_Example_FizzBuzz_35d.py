# gm_Example_FizzBuzz_35e: coded by Kinya MIURA 230414
# Fizz Buzz Problem: plan 35E **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan 35E ***  with 9 columns, 10 numbers in a line')
print('# -----------------------------------------------------------------------------')

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print(' FizzBuzz', end='')  # with 9 columns
    elif i % 3 == 0:
        print('     Fizz', end='')  # with 9 columns
    elif i % 5 == 0:
        print('     Buzz', end='')  # with 9 columns
    else:
        print(f'{i:9d}', end='')
    if i % 10 == 0:  # 10 numbers in a line
        print()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan 35E ***  with 9 columns, 10 numbers in a line
# -----------------------------------------------------------------------------
        1        2     Fizz        4     Buzz     Fizz        7        8     Fizz     Buzz
       11     Fizz       13       14 FizzBuzz       16       17     Fizz       19     Buzz
     Fizz       22       23     Fizz     Buzz       26     Fizz       28       29 FizzBuzz
'''
