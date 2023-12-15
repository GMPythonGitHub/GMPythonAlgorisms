# gm_Example_FizzBuzz_35E: coded by Kinya MIURA 230414
# Fizz Buzz Problem: plan 35E **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan 35E ***  building a large-sized string')
print('# -----------------------------------------------------------------------------')

stl = ''
for i in range(1,31):
    st = ''
    if i % 3 == 0:
        st += 'Fizz'
    if i % 5 == 0:
        st += 'Buzz'
    if st == '':
        st += str(i)
    stl += f'{st:>9s}'  # with 9 columns
    if i % 10 == 0:  # 10 numbers in a line
        stl += '\n'
print(stl, end='')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan 35E ***  building a large-sized string
# -----------------------------------------------------------------------------
        1        2     Fizz        4     Buzz     Fizz        7        8     Fizz     Buzz
       11     Fizz       13       14 FizzBuzz       16       17     Fizz       19     Buzz
     Fizz       22       23     Fizz     Buzz       26     Fizz       28       29 FizzBuzz
'''
