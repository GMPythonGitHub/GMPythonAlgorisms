# gm_FizzBuzz_Buzz_10col: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Fizz Buzz problem: checking Buzz, in 10 columns ***')

# =========================================================
for i in range(1,31):
    if i % 5 == 0:
        print(' Buzz', end='')  # with 5 columns
    else:
        print(f'{i:5d}', end='')  # with 5 columns
    if i % 10 == 0:  # 10 numbers in a row
        print()

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: checking Buzz, in 10 columns ***
    1    2    3    4 Buzz    6    7    8    9 Buzz
   11   12   13   14 Buzz   16   17   18   19 Buzz
   21   22   23   24 Buzz   26   27   28   29 Buzz
'''
