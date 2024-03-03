# gm_Secret_Number_multi: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Secret Number: multi numbers ***')
# ---------------------------------------------------------
import random

# =========================================================
## --- main routine --- ##
number_secret = random.randint(0, 99)
finish = False
while not finish:
    strgs = input('\tGuess the Secret Number (0-99):  ').split(',')
    numbers = [int(strg) for strg in strgs]
    for number in numbers:
        if number < number_secret:
            print(f'The Secret Number is greater than {number:02d} !!')
        elif number > number_secret:
            print(f'The Secret Number is less than {number:02d} !!')
        else:
            finish = True
            break
print(f'\t!!! You found the Secret Number:   {number_secret:02d} !!!')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Find seclet number: multi numbers ***
	Guess the Secret Number (0-99):  25,50,75
The Secret Number is less than 25 !!
The Secret Number is less than 50 !!
The Secret Number is less than 75 !!
	Guess the Secret Number (0-99):  5, 10, 15, 20
The Secret Number is greater than 05 !!
The Secret Number is greater than 10 !!
The Secret Number is greater than 15 !!
The Secret Number is greater than 20 !!
	Guess the Secret Number (0-99):  22, 24
	!!! You found the Secret Number:   22 !!!
'''