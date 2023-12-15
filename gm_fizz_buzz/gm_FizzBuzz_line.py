# gm_FizzBuzz_line: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Fizz Buzz problem: in a line ***')

# =========================================================
[print((' FizzBuzz' if i % 3 == 0 and i % 5 ==0 else '     Fizz' if i % 3 == 0 else '     Buzz' if i % 5 == 0 else f'{i:9d}'), ('\n' if i % 10 == 0 else ''), end='') for i in range(1, 31)]
#  with 9 columns, 10 numbers in a line

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: in a line ***
        1         2      Fizz         4      Buzz      Fizz         7         8      Fizz      Buzz 
       11      Fizz        13        14  FizzBuzz        16        17      Fizz        19      Buzz 
     Fizz        22        23      Fizz      Buzz        26      Fizz        28        29  FizzBuzz 
'''
