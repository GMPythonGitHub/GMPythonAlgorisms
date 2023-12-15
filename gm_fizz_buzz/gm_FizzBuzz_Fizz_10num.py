# gm_FizzBuzz_Fizz_5num: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Fizz Buzz problem: checking Fizz, 10 numbers in a row ***')

# =========================================================
for i in range(1,31):
    if i%3 == 0:
        print('Fizz ', end='')
    else:
        print(i,  end=' ')
    if i % 10 == 0:  # 10 numbers in a line
        print()

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: checking Fizz, 10 numbers in a row ***
1 2 Fizz 4 5 Fizz 7 8 Fizz 10 
11 Fizz 13 14 Fizz 16 17 Fizz 19 20 
Fizz 22 23 Fizz 25 26 Fizz 28 29 Fizz 
'''
