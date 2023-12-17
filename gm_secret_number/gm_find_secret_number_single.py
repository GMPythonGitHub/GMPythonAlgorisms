# gm_find_secret_number_single: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Find secret number: single number ***')
# ---------------------------------------------------------
import random

# =========================================================
## --- main routine --- ##
number_secret = random.randint(0, 99)

while True:
    number = int(input('\tGuess the Secret Number (0-99):  '))
    if number < number_secret:
        print('The Secret Number is greater than the Gess !!')
    elif number > number_secret:
        print('The Secret Number is less than the Guess !!')
    else:
        break
print(f'\t!!! You found the Secret Number:   {number_secret:02d} !!!')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Find seclet number ***
	Guess the Secret Number (0-99):  50
The Secret Number is greater than the Guess !!
	Guess the Secret Number (0-99):  75
The Secret Number is less than the Guess !!
	Guess the Secret Number (0-99):  67
The Secret Number is greater than the Guess !!
	Guess the Secret Number (0-99):  71
The Secret Number is less than the Guess !!
	Guess the Secret Number (0-99):  69
	!!! You found the Secret Number:   69 !!!
'''