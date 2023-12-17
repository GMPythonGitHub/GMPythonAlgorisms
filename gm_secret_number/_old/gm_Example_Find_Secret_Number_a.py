# gm_Example_Find_Secret_Number_a: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** ------------ ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import random
number_secret = random.randint(0, 99)

while True:
    number = int(input('\tGuess the Secret Number (0-99): '))
    if number > number_secret:
        print('The Number is greater than the Secret Number !!')
    elif number < number_secret:
        print('The Number is less than the Secret Number !!')
    else:
        break
print(f'\n\t!!! You found the Secret Number: {number_secret} !!!')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
	Guess the Secret Number (0-99): >? 50
The Number is less than the Secret Number !!
	Guess the Secret Number (0-99): >? 75
The Number is greater than the Secret Number !!
	Guess the Secret Number (0-99): >? 63
The Number is greater than the Secret Number !!
	Guess the Secret Number (0-99): >? 60
The Number is greater than the Secret Number !!
	Guess the Secret Number (0-99): >? 58
The Number is greater than the Secret Number !!
	Guess the Secret Number (0-99): >? 54
	!!! You found the Secret Number: 54 !!!
'''