# gm_prime_number_single_def: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Prime number: judging single number, definition ***')

# =========================================================
## --- main routine --- ##
num = 29
flg = False
for i in range(2, num):  # from 2 until num-1
    if num % i == 0:
        flg = True
        break
if flg:
    print(f'{num} is not a prime number!')
else:
    print(f'{num} is a prime number!')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Prime number: judging single number, definition ***
29 is a prime number!
'''