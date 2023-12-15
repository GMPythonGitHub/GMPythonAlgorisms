# gm_Example_FizzBuzz_35g: coded by Kinya MIURA 230414
# Fizz Buzz Problem: plan 35G **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan 35G ***  slicing a string')
print('# -----------------------------------------------------------------------------')

st = 'FizzBuzz'
for i in range(1, 31):
    st = 'FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8]  # slicing a string
    if len(st) == 0:
        st = str(i)
    print(f'{st:>9s}', end='')  # with 9 columns
    if i % 10 == 0:  # 10 numbers in a line
        print()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
** Fizz Buzz problem: Plan 35G ***  slicing a string
# -----------------------------------------------------------------------------
        1        2     Fizz        4     Buzz     Fizz        7        8     Fizz     Buzz
       11     Fizz       13       14 FizzBuzz       16       17     Fizz       19     Buzz
     Fizz       22       23     Fizz     Buzz       26     Fizz       28       29 FizzBuzz
'''
