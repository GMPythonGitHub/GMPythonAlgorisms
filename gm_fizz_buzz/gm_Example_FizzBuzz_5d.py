# gm_Example_FizzBuzz_5d: coded by Kinya MIURA 230414
# Fizz Buzz Problem: plan 5D **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan 5D ***  with 5 columns, 10 numbers in a line')
print('# -----------------------------------------------------------------------------')

for i in range(1,31):
    if i % 5 == 0:
        print(' Buzz', end='')  # with 5 columns
    else:
        print(f'{i:5d}', end='')  # with 5 columns
    if i % 10 == 0:  # 10 numbers in a row
        print()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan 5D ***  with 5 columns, 10 numbers in a line
# -----------------------------------------------------------------------------
    1    2    3    4 Buzz    6    7    8    9 Buzz
   11   12   13   14 Buzz   16   17   18   19 Buzz
   21   22   23   24 Buzz   26   27   28   29 Buzz
'''
