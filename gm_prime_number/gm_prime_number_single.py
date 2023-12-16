# gm_prime_number_single: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Prime number: judging single number ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
num = 29
flg = False
for i in range(2, int(np.sqrt(num))+1):  # from 2 until sqrt(num)-1
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
*** Prime number: judging single number ***
29 is a prime number!
'''