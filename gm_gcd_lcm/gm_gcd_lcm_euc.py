# gm_gcd_lcm_euc: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Greatest common divisor and Least common multiple ***')
print("   *** Euclid's algorithm ***")

# =========================================================
## --- main routine --- ##
numbera, numberb = 36, 120
print(f'{numbera = }, {numberb = }')
# greatest common divisor
numa, numb = numbera, numberb
gcd = lcm = 1
while True:
    if numa > numb:
        numa -= numb
    elif numb > numa:
        numb -= numa
    else:
        gcd = numa
        break
print(f'{gcd = }')
# least common multiple
numa, numb = numbera, numberb
while True:
    if numa > numb:
        numb += numberb
    elif numb > numa:
        numa += numbera
    else:
        lcm = numa
        break
print(f'{lcm = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Greatest common divisor and Least common multiple ***
   *** Euclid's algorithm ***
numbera = 36, numberb = 120
gcd = 12
lcm = 360
'''