# gm_gcd_lcm_euc_mdf: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Greatest common divisor and Least common multiple ***')
print("   *** Euclid's algorithm modified ***")

# =========================================================
## --- main routine --- ##
numbera, numberb = 36, 120
print(f'{numbera = }, {numberb = }')
# greatest common divisor
numa, numb = numbera, numberb
gcd = lcm = 1
while True:
    if numa > numb > 0:
        numa %= numb
        if numa == 0:
            gcd = numb
            break
    elif numb > numa > 0:
        numb %= numa
        if numb == 0:
            gcd = numa
            break
    elif numa == numb > 0:
        gcd = numa
        break
    else:
        gcd = 0
        break
print(f'{gcd = }')
# least common multiple
lcm = numbera * numberb // gcd
print(f'{lcm = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Greatest common divisor and Least common multiple ***
   *** Euclid's algorithm modified ***
numbera = 36, numberb = 120
gcd = 12
lcm = 360
'''